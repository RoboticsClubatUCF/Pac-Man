from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template;
from .models import Item
# Create your views here.
def home(request):
	return render(request,"inventory.html",
	{})

def search_inventory(request):
	if request.method == "POST":
		searched = request.POST['Search'] #returns what they searched
		#results = Item.objects.all()
		results = Item.objects.filter(name__contains=searched)
		num_results = results.count()
		return render(request,'Search_inventory.html',
		{'searched' : searched,
		'results' : results,
		'num_results': num_results})



# Create a view for lab location.
def lab_location(request):
	return HttpResponse("Inventory lab location page scaffold.")