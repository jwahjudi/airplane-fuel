from django.urls import path

from . import views 

urlpatterns = [
	path('', views.airplane, name='airplane'),
	path('airplane/', views.airplane_list),
	path('airplane/<int:pk>/', views.airplane_detail)
]