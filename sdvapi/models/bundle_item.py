from django.db import models
from .bundle import Bundle
from .item import Item

class BundleItem(models.Model):
  bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  quality = models.IntegerField()
