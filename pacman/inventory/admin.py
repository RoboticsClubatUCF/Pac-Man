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
    est_value
    image

BARCODE
    rccf_barcode
    ucf_barcode
    sale_barcode
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
                 'fields': ['est_value','image']
             }
         ),
         ('Barcodes',
             {
                 'fields': ['rccf_barcode','ucf_barcode','sale_barcode']
             }
         )
    ]


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
