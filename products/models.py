
from django.db import models

class ProductsModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    score = models.IntegerField(null=False, blank=False)
    image = models.CharField(max_length=100 ,null=False, blank=False)