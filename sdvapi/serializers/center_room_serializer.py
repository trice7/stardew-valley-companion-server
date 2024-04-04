from rest_framework import serializers
from sdvapi.models import CenterRoom

class CenterRoomSerializer(serializers.ModelSerializer):
  """JSON serializer for a center room"""
  
  class Meta:
    model = CenterRoom
    fields = ('id', 'name', 'reward', 'save')
    depth = 1
