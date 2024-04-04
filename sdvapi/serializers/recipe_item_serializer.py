from rest_framework import serializers
from sdvapi.models import RecipeItem

class RecipeItemSerializer(serializers.ModelSerializer):
  """JSON serializer for a Recipe Item"""
  
  class Meta:
    model = RecipeItem
    fields = ('id', 'item_needed', 'used_in')
