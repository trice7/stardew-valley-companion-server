from django.db import models
from .item_type import ItemType
from .perk import Perk

class Item(models.Model):
  name = models.CharField(max_length=30)
  type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
  grow_time = models.IntegerField()
  base_price = models.IntegerField()
  quality_modifier = models.BooleanField()
  perk_modifier = models.ForeignKey(Perk, on_delete=models.CASCADE)
  health = models.IntegerField()
  energy = models.IntegerField()
  acquired = models.CharField(max_length=100)
