from django.db import models


# Create your models here.
class dollar(models.Model):

   #name = models.CharField(max_length=100)

   #classification = models.CharField(max_length=100)

   #language = models.CharField(max_length=100)

   price = models.FloatField()
   stamp = models.CharField(max_length=100)
