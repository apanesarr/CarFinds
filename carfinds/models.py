from django.db import models
class Car(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.IntegerField()