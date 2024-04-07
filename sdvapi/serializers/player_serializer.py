from rest_framework import serializers
from sdvapi.models import Player

class PlayerSerializer(serializers.ModelSerializer):
  """JSON serializer for a player"""
  
  class Meta:
    model = Player
    fields = ('id', 'uid', 'username')
