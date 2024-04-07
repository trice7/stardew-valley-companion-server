from django.db import models
from .townie import Townie

class NPCEvent(models.Model):
  townie = models.ForeignKey(Townie, on_delete=models.CASCADE)
  unlock_condition = models.TextField()
  reward = models.CharField(max_length=200)
  path = models.TextField()
