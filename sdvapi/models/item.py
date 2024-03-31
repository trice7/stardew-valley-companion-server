from django.db import models
from .item_type import ItemType

class Item(models.Model):
  name = models.CharField(max_length=30)
  type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
  base_price = models.IntegerField()
  quality_modifier = models.BooleanField()
  health = models.IntegerField()
  energy = models.IntegerField()
  cost = models.IntegerField()
  acquired = models.CharField(max_length=100)
