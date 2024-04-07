from rest_framework import serializers
from sdvapi.models import Item

class ItemSerializer(serializers.ModelSerializer):
  """JSON serializer for an item"""
  
  class Meta:
    model = Item
    fields = ('id', 'name', 'type', 'grow_time', 'base_price', 'quality_modifier', 'perk_modifier', 'health', 'energy', 'acquired')
    depth = 1
