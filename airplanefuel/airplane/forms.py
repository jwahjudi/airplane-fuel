from django import forms

class IdForm(forms.Form):
	airplane_id = forms.IntegerField()