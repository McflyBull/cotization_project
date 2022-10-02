from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.utils import timezone

# Create your models here.

class Dollar(models.Model):
   price = models.FloatField()
   stamp = models.DateTimeField(default=timezone.now)