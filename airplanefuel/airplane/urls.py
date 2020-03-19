from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 

urlpatterns = [
	path('', views.airplane, name='airplane'),
	path('airplane/', views.AirplaneList.as_view()),
	path('airplane/<int:pk>/', views.AirplaneDetail.as_view()),
	path('airplane/<int:pk>/getConsumptionTime', views.getConsumptionTime),
	path('airplane/<int:pk>/getMaxFlyingTime', views.getMaxFlyingTime)
]
urlpatterns = format_suffix_patterns(urlpatterns)