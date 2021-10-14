from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hello world! Welcome to the inventory home page.")

# Create a view for lab location.
def lab_location(request):
	return HttpResponse("Inventory lab location page scaffold.")