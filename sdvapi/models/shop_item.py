from django.db import models
from .item import Item
from .shop import Shop

class ShopItem(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  cost = models.IntegerField()
