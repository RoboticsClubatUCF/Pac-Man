from django.db import models
from django.db.models.base import Model
from django.core.files.storage import FileSystemStorage
# Create your models here.


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
    # will be used later on in the query
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    general_type = models.CharField(
        blank=True, null=True, max_length=32, choices=GENERAL_TYPES)
    location = models.CharField(
        max_length=32, choices=GENERAL_LOCATIONS, blank=True, null=True)
    #image = models.ImageField(upload_to ="item_imgs",blank=True,null=True)

    def __str__(self):
        return self.name
