from rest_framework import serializers
from sdvapi.models import NPCEvent

class NPCEventSerializer(serializers.ModelSerializer):
  """JSON Serializer for an NPC event"""
  
  class Meta:
    model = NPCEvent
    fields = ('id', 'townie', 'unlock_condition', 'reward', 'path')
