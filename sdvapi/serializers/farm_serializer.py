from rest_framework import serializers
from sdvapi.models import Farm

class FarmSerializer(serializers.ModelSerializer):
  """JSON serializer for a farm"""
  
  class Meta:
    model = Farm
    fields = ('id', 'owner', 'name')
    depth = 1
    