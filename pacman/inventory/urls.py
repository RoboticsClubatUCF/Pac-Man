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
	path('location-map', views.lab_location, name='location')
] + static(MEDIA_URL,document_root=MEDIA_ROOT)
urlpatterns +=  staticfiles_urlpatterns()
