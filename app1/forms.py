from django import forms
from app1.models import Sensor1
class HomeForm(forms.ModelForm):

	state  = forms.CharField()
	# updated_date = forms.CharField()

	class Meta:
		model = Sensor1 
		fields = ('state',)