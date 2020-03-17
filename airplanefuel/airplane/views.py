from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import IdForm

def airplane(request):
	return HttpResponse("hello")

def details(request, airplane_id):


def get_airplane_id(request):
	if request.method == 'POST':
		form = IdForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks')
	else:
		form = IdForm()

	return render(request, '')
