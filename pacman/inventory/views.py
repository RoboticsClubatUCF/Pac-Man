from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Item
# Create your views here.


def home(request):
    return render(request, "inventory.html",
                  {})

# TODO
#  Find a way to search location foreign key, 
#    by having a var named "name" within 
#    the location model, or finding
#    some other solution to the issue 
def search_inventory(request):
    if request.method == "POST":
        searched = request.POST['Search']  # returns what they searched
        # results = Item.objects.all()
        names = Item.objects.filter(name__icontains=searched)
        generals = Item.objects.filter(general_type__icontains=searched)
        description = Item.objects.filter(description__icontains=searched)
        locations = Item.objects.select_related().filter()
        # [locations for items in names if str(items.location) == searched: locations= locations + items]
        results = names | generals | description #| locations 
        results = results.order_by('name')  # the start of sorting hell
        num_results = results.count()
        item_bio_page = False
        return render(request, 'search_inventory.html',
                      {'searched': searched,
                       'results': results,
                       'num_results': num_results,
                       'item_page':item_bio_page,
                       })


# TODO
#  Get a top down view of the lab's floor plan


def lab_location(request, item_id):
    searched_item = Item.objects.filter(id__contains=item_id).first()
    location_dir = str(searched_item.location)[:2]
    # The Goal here is to get the ability to search for similar items
    # other_items =
    return render(request, 'lab_location.html',
                  {
                      'searched': searched_item,
                      'dir_loc': location_dir,
                      # 'other_items': other_items,
                  })


def item_page(request, item_id):
    searched_item = Item.objects.filter(id__icontains=item_id)
    item_bio_page = True
    return render(request, 'search_inventory.html',  # swap Search_inventory.html to a new page
                  {
                      'searched': searched_item.first().name,
                      'results': searched_item,
                      'item_page':item_bio_page,
                  })
