from django.db import models

class Season(models.Model):
  name = models.CharField(max_length=10)
  icon = models.CharField(max_length=300)
