from django.db import models
from .season import Season

class Townie(models.Model):
  name = models.CharField(max_length=25)
  icon = models.CharField(max_length=300)
  birth_month = models.ForeignKey(Season, on_delete=models.CASCADE)
  birth_day = models.IntegerField()
  love_interest = models.BooleanField()
