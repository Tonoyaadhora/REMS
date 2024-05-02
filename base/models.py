from django.db import models

# Create your models here.
class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    property_address = models.CharField(max_length=100)
    property_size = models.IntegerField(default=0)
    property_bedroom = models.IntegerField(default=0)
    property_bathroom = models.IntegerField(default=0)
    rent_amount = models.IntegerField(default=0)
    status = models.CharField(max_length=100)