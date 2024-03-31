from django.db import models
from .player import Player

class Farm(models.Model):
  owner = models.ForeignKey(Player, on_delete=models.CASCADE)
  name = models.CharField(max_length=20)
