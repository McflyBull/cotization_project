from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Dollar(models.Model):
   price = models.FloatField()
   stamp = models.DateTimeField(default=datetime.now,)