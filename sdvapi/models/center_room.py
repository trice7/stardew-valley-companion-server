from django.db import models
from .farm import Farm

class CenterRoom(models.Model):
  name = models.CharField(max_length=25)
  reward = models.CharField(max_length=50)
  save = models.ForeignKey(Farm, on_delete=models.CASCADE)
