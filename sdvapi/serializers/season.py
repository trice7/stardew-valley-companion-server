from rest_framework import serializers
from sdvapi.models import Season

class SeasonSerializer(serializers.ModelSerializer):
  """JSON serializer for a season"""
  
  class Meta:
    model = Season
    fields = ('id', 'name', 'icon')
