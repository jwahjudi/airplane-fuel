from django.urls import path

from . import views 

urlpatterns = [
	path('', views.airplane, name='airplane'),
	path('<int:airplane_id>', views.detail, name='detail')
]