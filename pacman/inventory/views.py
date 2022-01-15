from django.shortcuts import render
from .models import Item
from pacman.settings import ITEMS_PER_PAGE
# Create your views here.


def home(request):
    return render(request, "inventory.html",
                  {})


def search_inventory(request, query=None, pageid=0):
    items_per_page = ITEMS_PER_PAGE
    searched = ""

    if query:
        searched = query
    else:
        searched = request.POST['Search']
    names = Item.objects.filter(name__icontains=searched)
    generals = Item.objects.filter(general_type__icontains=searched)
    description = Item.objects.filter(description__icontains=searched)
    location = Item.objects.filter(location__name__icontains=searched)

    results = names | generals | description | location
    results = results.order_by('name')
    num_results = results.count()
    num_pages = 1
    if (num_results > items_per_page):
        num_ = num_results
        while(num_ > items_per_page):
            num_pages += 1
            num_ -= items_per_page
    num_pages_ = range(0, num_pages)
    from_ = 0
    to_ = items_per_page
    if pageid > 0:
        from_ = pageid * items_per_page
        to_ = (pageid + 1) * items_per_page
        results = results[from_:to_]

    else:
        results = results.order_by("name")[:items_per_page]
    item_bio_page = False
    return render(request, 'search_inventory.html',
                  {'searched': searched,
                   'results': results,
                   'num_results': num_results,
                   'item_page': item_bio_page,
                   'pages': num_pages_,
                   })


# TODO
#  Get a !UPDATED! top down view of the lab's floor plan


def lab_location(request, item_id):
    searched_item = Item.objects.filter(id__contains=item_id).first()
    location_dir = str(searched_item.location)[:2]
    other_items = Item.objects.filter(
        location__name__icontains=searched_item.location)
    return render(request, 'lab_location.html',
                  {
                      'searched': searched_item,
                      'dir_loc': location_dir,
                      'other_items': other_items,
                  })




def items__at_location(request, location_tag):
    location_dir = str(location_tag)
    other_items = Item.objects.filter(location__name__icontains=location_dir)
    return render(request, 'items_at_locations.html',
                  {
                      'dir_loc': location_dir,
                      'other_items': other_items,
                  })


def item_page(request, item_id):
    searched_item = Item.objects.filter(id__icontains=item_id)
    item_bio_page = True
    return render(request, 'search_inventory.html',  # swap Search_inventory.html to a new page
                  {
                      'searched': searched_item.first().name,
                      'results': searched_item,
                      'item_page': item_bio_page,
                  })
