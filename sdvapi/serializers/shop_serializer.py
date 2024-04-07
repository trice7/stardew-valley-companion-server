from rest_framework import serializers
from sdvapi.models import Shop

class ShopSerializer(serializers.ModelSerializer):
  """JSON serializer for a shop"""
  
  class Meta:
    model = Shop
    fields = ('id', 'shopkeep', 'location')
    depth = 1
