from rest_framework import serializers
from sdvapi.models import Perk

class PerkSerializer(serializers.ModelSerializer):
  """JSON serializer for perks"""
  
  class Meta:
    model = Perk
    fields = ('id', 'label', 'effect', 'skill')
    depth = 1
