from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.db import models
from .models import Item,Location

class LocationAdmin(admin.ModelAdmin):
    model = Location
    exclude = ('name',)

class ItemAdmin(admin.ModelAdmin):
    model = Item
    fieldsets = [
        ('General Info',
        {
            'fields': ['name','description','quantity']
        }
        ),(
            'Type & Location',{'fields':['general_type','location']}
        )
    ]

# Register your models here.
admin.site.register(Item,ItemAdmin)
admin.site.register(Location,LocationAdmin)