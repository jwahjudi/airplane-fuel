from django.urls import reverse
from django.test import TestCase, Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Airplane
from .serializers import AirplaneSerializer

client = Client()

class GetAllAirplanes(TestCase):
	def setUp(self):
		Airplane.objects.create(id=1, passengers=1)
		Airplane.objects.create(id=2, passengers=1)
		Airplane.objects.create(id=3, passengers=1)
		Airplane.objects.create(id=4, passengers=1)
		Airplane.objects.create(id=5, passengers=1)
		Airplane.objects.create(id=6, passengers=1)
		Airplane.objects.create(id=7, passengers=1)
		Airplane.objects.create(id=8, passengers=1)
		Airplane.objects.create(id=9, passengers=1)
		Airplane.objects.create(id=10, passengers=1)

	def test_get_all_airplanes(self):
		response = client.get(reverse('airplanes'))
		airplanes = Airplane.objects.all()
		serializer = AirplaneSerializer(airplanes, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
