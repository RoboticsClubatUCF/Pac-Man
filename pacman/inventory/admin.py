from django.contrib import admin
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