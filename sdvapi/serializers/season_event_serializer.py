from rest_framework import serializers
from sdvapi.models import SeasonEvent

class SeasonEventSerializer(serializers.ModelSerializer):
  """JSON serializer for a season event"""
  
  class Meta:
    model = SeasonEvent
    fields = ('id', 'month', 'day', 'description')
    depth = 1
