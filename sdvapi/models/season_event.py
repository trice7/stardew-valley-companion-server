from django.db import models
from .season import Season

class SeasonEvent(models.Model):
  month = models.ForeignKey(Season, on_delete=models.CASCADE)
  day = models.IntegerField()
  description = models.TextField()
