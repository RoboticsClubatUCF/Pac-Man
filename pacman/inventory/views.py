from datetime import date, timedelta, datetime
from distutils.log import warn
import enum
from itertools import count
from pydoc import describe
from django.shortcuts import render
from .models import Item
from pacman.settings import ITEMS_PER_PAGE
# Create your views here.


class item_condition (enum.Enum):
    Cannibalized = 0
    Obsolete = 1
    Poor = 2
    Fair = 3
    Excellent = 4
    New = 5


def home(request):
    ex_items = 0
    w_items = 0
    err_items = 0

    '''for i in Item.objects.all():
        # Check if an item is expired
        if ((i.exp_date - date.today()) <= timedelta(0, 0)):
            ex_items += 1
        # Check if an item has some missing, but usefull informaton
        if (i.description == None or len(str(i.description)) < 5 or i.quantity == None or i.location == None):  # needs to be tested
            w_items += 1
        # Check if an item has an important Issue'''
    return render(request, "inventory.html",
                  {
                    'exp_items': ex_items,  # exp_items.count(),
                    'warn_items': w_items,  # warn_items.count(),
                    'error_items': err_items,  # error_items.count(),
                    'home': True
                  })


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

    rccf_bar = Item.objects.filter(rccf_barcode__icontains=searched)
    ucf_bar = Item.objects.filter(ucf_barcode__icontains=searched)
    sale_bar = Item.objects.filter(sale_barcode__icontains=searched)

    results = names | generals | description | location | rccf_bar | ucf_bar | sale_bar
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


def lab_location(request, item_id):
    searched_item = Item.objects.filter(id__contains=item_id).first()
    full_loc = str(searched_item.location)
    location_dir = str(searched_item.location)[:2].lower()
    if (location_dir[0] == 'l'):
        location_dir = 'L'
    location_first_l = str(searched_item.location)[0]
    other_items = Item.objects.filter(
        location__name__icontains=searched_item.location)
    return render(request, 'lab_location.html',
                  {
                      'searched': searched_item,
                      'dir_loc': location_dir,
                      'full_loc': full_loc,
                      'other_items': other_items,
                      'first_l': location_first_l,
                  })


def items_at_location(request, location_tag):
    location_dir = str(location_tag)
    other_items = Item.objects.filter(location__name__icontains=location_dir)
    return render(request, 'items_at_locations.html',
                  {
                      'dir_loc': location_dir,
                      'other_items': other_items,
                  })


def item_page(request, item_id):
    searched_item = Item.objects.filter(id__icontains=item_id)
    return render(request, 'item_profile.html',  # swap Search_inventory.html to a new page
                  {
                      'item_name': searched_item.first().name,
                      'item': searched_item.first(),
                  })


def items_with_condition(request, c=123450):
    # c is the condition state
    # 0 is Cannibalized
    # 1 is Obsolete
    # 2 is Poor
    # 3 is Fair
    # 4 is Excellent
    # 5 is New
    # Error Found :
    #   if c = any int starting with '0' it will not be handled
    #

    # C can be a number > 5 to combine searches
    # example :
    #   012 / 120 / 201 Etc,
    #   this string of nums should give results for any item that is
    #   Cannibalized or Obsolete or Poor
    #   This should be handled by checking if C is > 5
    # There will be no pagination for this,
    #    because the number of items in this state should be minimal
    result = Item.objects.none()  # this is for initial Declaration
    # init declaration :
    s0 = False
    s1 = False
    s2 = False
    s3 = False
    s4 = False
    s5 = False
    # expand this system to include items with warnings, or with errors, or that are expired
    if (c > 8 or not str(c).__len__.__eq__(0)):
        query = str(c)
        for search in query:
            if int(search) == 0:
                s0 = True
            elif int(search) == 1:
                s1 = True
            elif int(search) == 2:
                s2 = True
            elif int(search) == 3:
                s3 = True
            elif int(search) == 4:
                s4 = True
            elif int(search) == 5:
                s5 = True
            result = result | Item.objects.filter(
                condition__icontains=item_condition(int(search)).name)
    else:
        if int(c) == 0:
            s0 = True
        elif int(c) == 1:
            s1 = True
        elif int(c) == 2:
            s2 = True
        elif int(c) == 3:
            s3 = True
        elif int(c) == 4:
            s4 = True
        elif int(c) == 5:
            s5 = True
        result = Item.objects.filter(
            condition__icontains=item_condition(int(c)).name)
    return render(request, 'search_conditions.html',
                  {
                      'results': result,
                      's0': s0,
                      's1': s1,
                      's2': s2,
                      's3': s3,
                      's4': s4,
                      's5': s5,
                  })


def notification_table(request):
    _old = "1999-01-01"
    
    expired = Item.objects.filter(exp_date__range=[_old,str(datetime.today().date())])
    items = expired
    return render(request,'notifications.html',
    {
        'items':items
    })
def search_ByValue(request):
    value = 0
    for i in Item.objects.all():
        if i.est_value is not None:
            value += float(i.est_value) * float(i.quantity)
            value = round(value,2)
    return render(request,"search_value.html",{
        'value':value
    })