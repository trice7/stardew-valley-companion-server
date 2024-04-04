from django.db import models
from .townie import Townie

class Shop(models.Model):
  shopkeep = models.ForeignKey(Townie, on_delete=models.CASCADE)
  location = models.CharField(max_length=50)
