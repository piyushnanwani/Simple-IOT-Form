from .models import Sensor1Client
from django.views.generic import TemplateView
from app1.forms import HomeForm
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse, HttpRequest
from app1.models import Sensor1
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

from django.views.decorators.csrf import csrf_exempt
class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self,request):
		form = HomeForm()
		return render(request, self.template_name,{'form':form})


	# @csrf_protect
	def post(self,request):
		form = HomeForm(request.POST) 	
		print(form)
		if form.is_valid():
			form.save()
			# post = form.save(commit=False) # I want do something with object before saving form
			# post.save

			text = form.cleaned_data['state']
			# form = HomeForm()
			# return redirect['app1:app1']
			
		args = {'form':form, 'text':text}
		return render(request, self.template_name,args)

from django.db import connection

def my_custom_sql():
	with connection.cursor() as cursor:
	    myans = cursor.execute("SELECT state from app1_sensor1")
	    # -- cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
	    # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
	    # row = cursor.fetchone()


	return myans


def myviewfunction2(request):
	return HttpResponse("ON",content_type="application/liquid; charset=utf-8")


# TO return a state to a view of Page.
# Working!!!!!!!!!!!!!!-------------------------->
# But still returning <Response 200>
def myviewfunction3(request):
	

	# final_state = '';
	# for cur_state in Sensor1.objects.raw('SELECT * FROM app1_sensor1'):
	# 	# print(cur_state)
	# 	# print(cur_state)
	# 	final_state = final_state + '\n' + str(cur_state)
	final_state = Sensor1.objects.all()[4].state
	# final_state = my_custom_sql()
	return HttpResponse(final_state)

# Returning <Response 200>	
def myviewfunction8(request):
	return HttpResponse("ON", content_type="text/plain charset=utf-8")


# Error Template does not exist!
def myviewfunction4(request):
	response = "ON "
	return render(request,response)


# file containing content is downloaded.
def myviewfunction6(request):
	# Method 1
	# content = '<html>test123</html>'
	content = "ON"

	response = HttpResponse(content, content_type="application/liquid; charset=utf-8")
	response['Content-Length'] = len(content)

	return response
	
def myviewfunction7(request):
	response = "ON "
	return render_to_response(request,response)

# def myviewfunction(request):
# 	response = "ON "
# 	return get_object_or_404(Sensor1,pk=1)



# Final function ----------------------------->
#  Final           !!!!!!!!!!!!!!!


def myviewfunction(request):
	total_len = len(Sensor1.objects.all())
	final_state = Sensor1.objects.all()[total_len-1].state
	
	return HttpResponse(final_state ,content_type="text/plain charset=utf-8" )

def home2(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()

    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

import re
# from .models import Sensor1Client  # imported above 
def yourviewfunction(HttpRequest):
	string = "motherFucka"
	mylist =''
	if(HttpRequest.method == 'POST'):
		# string = HttpRequest.body  Error since storing bytes in a string, you first need to decode
		string = HttpRequest.body.decode("utf-8")

		# mylist = re.split('; |,|\*|\n', string)
		mylist = re.split(',', string) #removing commas from CSV format & converting it into a list
		# for i in mylist:
			# print(i)
		sensor1client_instance = Sensor1Client.objects.create(sensor_name=mylist[0],state=mylist[1], time=mylist[2])


	return HttpResponse("Sucessfully following data to the table : " + string)

#from django.db import connection
def yourviewfunction_table2(request):
	cursor = connection.cursor()
	# result = cursor.execute('''SELECT count(*) FROM app1_sensor1client''')
	total_len = len(Sensor1Client.objects.all())
	final_state = Sensor1Client.objects.all()
	result_response=""
	for item in Sensor1Client.objects.all():
		result_response = result_response + item.sensor_name + " "  + item.state + " " + item.time + "\n"
	return HttpResponse(result_response ,content_type="text/plain charset=utf-8" )
	# return HttpResponse(Sensor1Client.objects.raw('SELECT * FROM app1_sensor1client'), content_type="text/plain charset=utf-8")

def yourviewfunction_table(request):
	final_state = Sensor1Client.objects.all()
	return render_to_response(final_state, context_instance=RequestContext(request))
	# return HttpResponse(Sensor1Client.objects.raw('SELECT * FROM app1_sensor1client'), content_type="text/plain charset=utf-8")
