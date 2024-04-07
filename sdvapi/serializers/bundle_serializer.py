from rest_framework import serializers
from sdvapi.models import Bundle

class BundleSerializer(serializers.ModelSerializer):
  """JSON serializer for a bundles items"""
  
  class Meta:
    model = Bundle
    fields = ('id', 'name', 'image', 'room', 'items_needed', 'reward', 'reward_amount')
    depth = 1
