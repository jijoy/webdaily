'''
Created on Feb 21, 2016

@author: jijoy
'''
from google.appengine.ext import  ndb, db


   
class Data(db.Model):
    
    
    
    created = db.DateTimeProperty(auto_now_add=True)
    user_id = db.StringProperty()
    text = db.StringProperty()
    option1 = db.IntegerProperty()
    option2 = db.IntegerProperty()
    

    
 