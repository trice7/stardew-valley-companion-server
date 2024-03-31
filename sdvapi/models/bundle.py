from django.db import models
from .center_room import CenterRoom

class Bundle(models.Model):
  name = models.CharField(max_length=30)
  image = models.CharField(max_length=300)
  room = models.ForeignKey(CenterRoom, on_delete=models.CASCADE)
  items_needed = models.IntegerField()
  reward = models.CharField(max_length=30)
  reward_amount=models.IntegerField()
