from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Dollar(models.Model):


   #name = models.CharField(max_length=100)


   #classification = models.CharField(max_length=100)


   #language = models.CharField(max_length=100)

   price = models.FloatField()

   stamp = models.DateTimeField(default=datetime.now,)