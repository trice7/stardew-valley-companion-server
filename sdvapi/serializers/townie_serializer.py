from rest_framework import serializers
from sdvapi.models import Townie

class TownieSerializer(serializers.ModelSerializer):
  """JSON serializer for a townie"""
  
  class Meta:
    model = Townie
    fields = ('id', 'name', 'icon', 'birth_month', 'birth_day', 'love_interest')
