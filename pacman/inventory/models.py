from django.db import models
from django.db.models.base import Model
# Create your models here.
# Do not migrate this model, needs to be updated to new room design and new arch
#  of how things will be categorized
# MACRO_LOCATIONS = [
#     ('T','Table'),
#     ('R','Rack'),
#     ('C','Cabinet'),
#     ('B','WorkBench'),
# ]
# SUB_LOCATIONS = [
#     ('S','Shelf'),
#     ('U','Underneath'),
# ]


def location_id_fix(a):
    if (str(a) == "None"):
        return ""
    else:
        return a


class Location(Model):
    MACRO_LOCATIONS = [
        ('T', 'Table'),
        ('R', 'Rack'),
        ('C', 'Cabinet'),
        ('B', 'WorkBench'),
    ]
    SUB_LOCATIONS = [
        ('S', 'Shelf'),
        ('U', 'Underneath'),
    ]
    macro_location = models.CharField(
        max_length=1, null=True, blank=True, choices=MACRO_LOCATIONS)
    macro_location_id = models.IntegerField(null=True, blank=True)
    micro_location = models.CharField(
        max_length=1, null=True, blank=True, choices=SUB_LOCATIONS)
    micro_location_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.macro_location + str(location_id_fix(self.macro_location_id)) + self.micro_location + str(location_id_fix(self.micro_location_id))


class Item(Model):
    GENERAL_TYPES = [
        ('Electronics', 'ELECTRONICS'),
        ('Raw Material', 'RAW MATERIAL'),
        ('Hand Tool', 'HAND TOOL'),
        ('Safety Equipment', 'SAFETY EQUIPMENT'),
        ('Power Tool', 'POWER TOOL'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True, null=True)
    quantity = models.IntegerField()
    general_type = models.CharField(
        blank=True, null=True, max_length=32, choices=GENERAL_TYPES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True,
                                 null=True, help_text="Location(s) this item can be found at")
    #image = models.ImageField(upload_to ="item_imgs",blank=True,null=True)
    
    def __str__(self):
        return self.name + "  -  " + str(self.location)
