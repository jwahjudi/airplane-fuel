from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import AirplaneSerializer
from .models import Airplane

def airplane_list(request):
	if request.method =='GET':
		airplane = Airplane.objects.all()
		serializer = AirplaneSerializer(airplane, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method =='POST':
		data = JSONParser().parse(request)
		serializer = AirplaneSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

def airplane_detail(request, pk):
	try:
		airplane = Airplane.objects.get(pk=pk)
	except Airplane.DoesNotExist:
		return HttpResponse(status=404)

	if request.method =='GET':
		serializer = AirplaneSerializer(airplane)
		return JsonResponse(serializer.data)

	elif request.method =='POST':
		data = JSONParser().parse(request)
		serializer = AirplaneSerializer(airplane, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		airplane.delete()
		return HttpResponse(status=204)

def airplane(request):
	return HttpResponse("hello")

