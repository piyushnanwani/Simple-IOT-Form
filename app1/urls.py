from django.conf.urls import url
from app1.views import HomeView
from . import views
from django.urls import path, include
urlpatterns = [
	path('home', HomeView.as_view(), name='home'),
	path('myview', views.myviewfunction, name='myview'),
	path('yourview', views.yourviewfunction, name='yourview'),
	path('yourviewdata', views.yourviewfunction_table2, name='yourviewdata'),


	# path('first', views.first, name='first'),
	# path('sensor_form', views.sensor_form, name='sensor_form'),
	# path('sensor_form', views.FormView().get, name='sensor_form'),
	# path('resume', views.resume, name='resume'),
	# path('', views.index, name='index'),
]