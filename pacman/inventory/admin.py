from django.contrib import admin
from .models import Item, Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    exclude = ('name',)
    ordering = ['name']


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


@admin.action(description="Remove registered location")
def remove_location(modeladmin, request, queryset):
    queryset.update(location=None)


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['name', 'location', 'quantity','est_value', 'condition','exp_date']
    ordering = ['name']
    actions = [remove_location]
    fieldsets = [
        ('General Info',
            {
                'fields': ['name', 'description', 'quantity', 'condition']
            }
         ),
        ('Type & Location',
            {
                'fields': ['general_type', 'location']
            }
         ),
        ('Misc',
            {
                'fields': ['est_value', 'exp_date', 'image']
            }
         ),
        ('Barcodes',
            {
                'fields': ['yellow_tag', 'rccf_barcode', 'ucf_barcode', 'sale_barcode']
            }
         )
    ]


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
