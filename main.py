import webapp2
from google.appengine.api import users
import json
import jinja2
from model.models import Data
import time
from google.appengine.ext import db
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class UIHandler(webapp2.RequestHandler):
    def get(self):
        url_fragments = self.request.path.lstrip('').split('/')
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
        else:
            url = users.create_login_url('/')
        
        api_name = url_fragments[-1].strip() 
        
        if api_name == 'add':
            template = JINJA_ENVIRONMENT.get_template('add.html')
            html = template.render({}) 
        elif api_name == 'update':
            template = JINJA_ENVIRONMENT.get_template('update.html')
            html = template.render({})
        elif api_name == 'search':
            template = JINJA_ENVIRONMENT.get_template('search.html')
            html = template.render({})
        elif api_name == 'delete':
            template = JINJA_ENVIRONMENT.get_template('delete.html')
            html = template.render({})

        else:
            template = JINJA_ENVIRONMENT.get_template('home.html')
            html = template.render({'user':user, 'url':url})
        
        self.response.write(html)      

class APIHandler(webapp2.RequestHandler):
    def get(self):
        url_fragments = self.request.path.lstrip('').split('/')
        api_name = url_fragments[-1].strip() 
        user = users.get_current_user()
        
        if api_name == 'add':
            textvalue = self.request.get('t')
            op1 = self.request.get('op1')
            op2 = self.request.get('op2')
            if textvalue and op1 and op2 :
                data = Data()
                data.text = textvalue
                data.user_id = user.user_id()
                data.option1 = int(op1)
                data.option2 = int(op2)
                data.put()
                time.sleep(1)
 
        elif api_name == 'update':
            op1 = self.request.get('op1')
            op1new = self.request.get('op1new')
            if op1 and op1new :
                data = Data().all().filter('option1', int(op1))
                if data:
                   for d in data:
                       d.option1 = int(op1new)
                       d.save()
                time.sleep(1)

            
 
              
        elif api_name == 'search':
            op1 = self.request.get('op1')
            print op1
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(self.get_records(op1))               
        elif api_name == 'delete':
            op1 = self.request.get('op1')
            if op1  :
                data = Data().all().filter('option1', int(op1))
                if data:
                   for d in data:
                       d.delete()
            time.sleep(1)
 
        
    def get_records(self, op1):
#         for data in Data.all():
        response = []
        if op1:
            op1 = int(op1)
            for data in Data.all().filter('option1', op1):
                print 'Found'
                response.append({'text':data.text, 'option1':data.option1, 'option2':data.option2})
            return json.dumps(response)
            
        else :
       
            for data in Data.all():
                print data.option1
                response.append({'text':data.text, 'option1':data.option1, 'option2':data.option2})
            return json.dumps(response)
    
    
           
        
     
app = webapp2.WSGIApplication([
  ('/api/.*', APIHandler),
  ('/.*', UIHandler),
], debug=True)
