from django.db import models
from .item import Item

class RecipeItem(models.Model):
  item_needed = models.ForeignKey(Item, on_delete=models.CASCADE)
  used_in = models.ForeignKey(Item, on_delete=models.CASCADE)
