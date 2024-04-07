"""View Module for handling requests for a season event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import SeasonEvent
from sdvapi.serializers import SeasonEventSerializer

class SeasonEventView(ViewSet):
  """SDVCompanion Season Event View"""
  
  def retrieve(self, request, pk):
    """Handles GET reqeusts for a single Event
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      event = SeasonEvent.objects.get(pk=pk)
      serializer = SeasonEventSerializer(event)
      return Response(serializer.data)
    except SeasonEvent.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
