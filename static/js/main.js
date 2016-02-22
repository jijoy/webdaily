$(document).ready(function(){
	
	$('#add-form').submit(function(e){
		e.preventDefault();
		var text = $('#t').val();
		var op1v = $('#op1').val();
		var op2v = $('#op2').val();
		$.get("/api/add",{t:text,op1:op1v,op2:op2v}).done(function(data){
			$.get("/api/search").done(function(data){
				$('#results-list').empty();
				$.each(data, function(key,value) {
					
					$('#results-list').append('<li>'+value.text+','+value.option1+','+value.option2+'</li>')
				});
				
			});
			
		});		
		
	});
	$('#update').submit(function(event){
		event.preventDefault();
		var op1v = $('#op1').val();
		var opt1newv = $('#op1new').val();
		$.get("/api/update",{op1:op1v,op1new:opt1newv}).done(function(data){
			$.get("/api/search").done(function(data){
				$('#results-list').empty();
				$.each(data, function(key,value) {
					
					$('#results-list').append('<li>'+value.text+','+value.option1+','+value.option2+'</li>')
				});
				
			});
			
		});			
	});
	$('#delete').submit(function(event){
		event.preventDefault();
		var op1v = $('#op1').val();
		$.get("/api/delete",{op1:op1v}).done(function(data){
			$.get("/api/search").done(function(data){
				$('#results-list').empty();
				$.each(data, function(key,value) {
					
					$('#results-list').append('<li>'+value.text+','+value.option1+','+value.option2+'</li>')
				});
				
			});
			
		});	
	});	
	$('#search').submit(function(event){
		event.preventDefault();
		var op1v = $('#op1').val();
		$.get("/api/search",{op1:op1v}).done(function(data){
			$('#results-list').empty();
			$.each(data, function(key,value) {
				$('#results-list').append('<li>'+value.text+','+value.option1+','+value.option2+'</li>')
			});
			
		});		
	});		
});