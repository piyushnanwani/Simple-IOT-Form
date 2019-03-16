from django.db import models
from django.contrib.auth.models import User

class Sensor1(models.Model):
	# id = models.CharField(primary_key=True,max_length=10)
	state  = models.CharField('LED State',max_length=4)
	# updated_date = models.CharField('Updated Date', max_length=10)

class Sensor1Client(models.Model):
	sensor_name = models.CharField('Sensor name',max_length=10)
	state  = models.CharField('LED State',max_length=4)
	time  = models.CharField('time instant',max_length=35)
