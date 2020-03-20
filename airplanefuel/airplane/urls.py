from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'airplane', views.AirplaneViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('airplane/<int:pk>/getConsumptionTime/', views.getConsumptionTime),
	path('airplane/<int:pk>/getMaxFlyingTime/', views.getMaxFlyingTime)
]