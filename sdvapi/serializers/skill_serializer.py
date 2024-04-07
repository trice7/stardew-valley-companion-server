from rest_framework import serializers
from sdvapi.models import Skill

class SkillSerializer(serializers.ModelSerializer):
  """JSON serializer for a skill"""
  
  class Meta:
    model = Skill
    fields = ('id', 'label', 'activated')
