from rest_framework import serializers
from sdvapi.models import ShopItem

class ShopItemSerializer(serializers.ModelSerializer):
  """JSON serializer for a shop item"""
  
  class Meta:
    model = ShopItem
    fields = ('id', 'shop', 'item', 'cost')
    depth = 1
