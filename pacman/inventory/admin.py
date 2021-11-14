from django.contrib import admin
from .models import Item,Location

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['macro location','micro location']

class ItemAdmin(admin.ModelAdmin):
    model = Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Location)