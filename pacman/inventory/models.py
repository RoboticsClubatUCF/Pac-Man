from django.db import models
from django.db.models.base import Model
# Create your models here.
class Item(Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    description = models.CharField(max_length=256)
    def __str__(self):
        return self.name