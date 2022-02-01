from django.contrib import admin
from .models import Item, Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    exclude = ('name',)


"""
GENERAL INFO
    name
    description
    quantity
    condition

TYPE & LOCATION
    general_type
    location

MISC
    barcode_id
    est_value
    image
"""



class ItemAdmin(admin.ModelAdmin):
    model = Item
    fieldsets = [
        ('General Info',
            {
                 'fields': ['name', 'description', 'quantity','condition']
            }
         ),
        ('Type & Location',
            {
                 'fields': ['general_type', 'location']
            }
         ),
         ('Misc',
             {
                 'fields': ['est_value','barcode_id']
             }
         )
    ]


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
