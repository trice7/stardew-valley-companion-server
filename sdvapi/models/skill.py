from django.db import models

class Skill(models.Model):
  label = models.CharField(max_length=25)
  activated = models.BooleanField()
