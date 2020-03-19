from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import AirplaneSerializer
from .models import Airplane

class AirplaneList(generics.ListCreateAPIView):
	queryset = Airplane.objects.all()
	serializer_class = AirplaneSerializer

class AirplaneDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Airplane.objects.all()
	serializer_class = AirplaneSerializer

def airplane(request):
	return HttpResponse("hello")

@api_view(['GET'])
def getConsumptionTime(request, pk):
	try:
		airplane = Airplane.objects.get(pk=pk)
	except Airplane.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	consumption_time = airplane.consumption_per_min
	return Response({
		"consumption_time_per_min": consumption_time
	})

@api_view(['GET'])
def getMaxFlyingTime(request, pk):
	try:
		airplane = Airplane.objects.get(pk=pk)
	except Airplane.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	max_flying_time = airplane.max_flying_time
	return Response({
		"max_flying_time_per_min": max_flying_time
	})

