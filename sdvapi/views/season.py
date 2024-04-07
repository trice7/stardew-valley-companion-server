"""View Module for handling requests for a season"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Season
from sdvapi.serializers import SeasonSerializer

class SeasonView(ViewSet):
  """SDVCompanion Season View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single season
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      season = Season.objects.get(pk=pk)
      serializer = SeasonSerializer(season)
      return(serializer.data)
    except Season.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request, pk):
    """Handles GET request for all Seasons
    
    Returns -> JSON serialized response -- 200 status"""
    
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)
    return Response(serializer.data)
