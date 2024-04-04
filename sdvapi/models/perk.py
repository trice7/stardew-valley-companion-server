from django.db import models
from .skill import Skill

class Perk(models.Model):
  label = models.CharField(max_length=25)
  effect = models.TextField()
  skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
