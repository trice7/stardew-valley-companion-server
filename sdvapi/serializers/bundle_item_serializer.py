from rest_framework import serializers
from sdvapi.models import BundleItem

class BundleItemSerializer(serializers.ModelSerializer):
  """JSON serializer for a bundles items"""
  
  class Meta:
    model = BundleItem
    fields = ('id', 'bundle', 'item', 'quantity', 'quality')
    depth = 1
