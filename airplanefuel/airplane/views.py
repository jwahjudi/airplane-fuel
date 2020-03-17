from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, permissions, generics

from .serializers import AirplaneSerializer
from .models import Airplane

class AirplaneViewSet(viewsets.ModelViewSet):
	queryset = Airplane.objects.all().order_by('-consumption_per_min')
	serializer_class = AirplaneSerializer

class ListAirplaneView(generics.ListAPIView):
	queryset = Airplane.objects.all()
	serializer_class = AirplaneSerializer

def airplane(request):
	return HttpResponse("hello")

def details(request, airplane_id):
	airplane = get_object_or_404(Airplane, pk=id)
	return render(request, '')

