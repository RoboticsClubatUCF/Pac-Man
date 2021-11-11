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
		names = Item.objects.filter(name__icontains=searched)
		generals = Item.objects.filter(general_type__icontains=searched)
		locations = Item.objects.filter(location__icontains=searched)
		description = Item.objects.filter(description__icontains=searched)
		results = names | generals | locations | description
		results = results.order_by('name') # the start of sorting hell
		num_results = results.count()
		return render(request,'search_inventory.html',
		{'searched' : searched,
		'results' : results,
		'num_results': num_results,
		})


# TODO 
#  Get a top down view of the lab's floor plan
#  Properly implement "desired_item" var
# Create a view for lab location.
def lab_location(request, item_id):
	searched_item = Item.objects.filter(id__icontains=item_id)
	return render(request,'lab_location.html',
	{
	'searched':searched_item,
	}) 

def item_page(request, item_id):
	searched_item = Item.objects.filter(id__icontains=item_id)
	return render(request,'search_inventory.html', # swap Search_inventory.html to a new page
	{
	'searched' : item_id,
	'results' : searched_item,
	'num_results': 1,
	})