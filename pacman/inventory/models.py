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


class Item(Model):
    GENERAL_LOCATIONS = [
        ('Electronics', 'Electronics'),
        ('Batteries', 'Batteries'),
        ('Raw Metals', 'Raw Metals'),
        ('Hand Tools', 'Hand Tools'),
        ('Safety Equipment', 'Safety Equipment'),
        ('Back Table', 'Back Table'),
        ('Lockers', 'Lockers'),
        ('Center Table', 'Center Table'),
        ('Computer Parts', 'Computer Parts'),
        ('Front Table', 'Front Table'),
    ]

    GENERAL_TYPES = [
        ('Electronics', 'ELECTRONICS'),
        ('Raw Material', 'RAW MATERIAL'),
        ('Hand Tool', 'HAND TOOL'),
        ('Safety Equipment', 'SAFETY EQUIPMENT'),
        ('Power Tool', 'POWER TOOL'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)
    quantity = models.IntegerField()
    general_type = models.CharField(
        blank=True, null=True, max_length=32, choices=GENERAL_TYPES)
    new_location = models.CharField(max_length=32,blank=True,null=True)
    location = models.CharField(
        max_length=32, choices=GENERAL_LOCATIONS, blank=True, null=True)
    #image = models.ImageField(upload_to ="item_imgs",blank=True,null=True)
    def __str__(self):
        return self.name
