from rest_framework import serializers
from sdvapi.models import ItemType

class ItemTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for an item type"""
  
  class Meta:
    model = ItemType
    fields = ('id', 'label')
