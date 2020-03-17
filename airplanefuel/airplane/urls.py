from django.urls import path

from . import views 
from .views import ListAirplaneView

urlpatterns = [
	path('', views.airplane, name='airplane'),
	path('songs/', ListAirplaneView.as_view(), name="airplane-all")
]