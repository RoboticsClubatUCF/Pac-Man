from django.urls import path
from pacman.settings import MEDIA_ROOT, MEDIA_URL
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = [
	path('', views.home, name='home'),
	path('search_inventory', views.search_inventory, name='search-inventory'),
	path('search_inventory/x/<str:query>/<int:pageid>', views.search_inventory, name='search-inventory2'),
	path('location_map/<int:item_id>', views.lab_location, name='location'), # for individual items
	path('location_map/x/<str:location_tag>',views.items_at_location, name='items_location'), # for when someone click on the location map, and wants to know what is there
	path('items/<int:item_id>', views.item_page, name='item-page'),
	path('condition/<int:c>',views.items_with_condition, name="items_condtions_list"),
	path('condition/',views.items_with_condition, name="items_condtions_list")

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
