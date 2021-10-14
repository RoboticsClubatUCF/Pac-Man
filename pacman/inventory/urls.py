from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('location-map', views.lab_location, name='location')
]