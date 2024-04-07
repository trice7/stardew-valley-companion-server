"""View Module for handling requests for an NPC event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import NPCEvent
from sdvapi.serializers import NPCEventSerializer

class NPCEventView(ViewSet):
  """SDVCompanion NPC Event View"""
  
  def retrieve(self, request, pk):
    """Handles GET reqeusts for a single Event
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      event = NPCEvent.objects.get(pk=pk)
      serializer = NPCEventSerializer(event)
      return Response(serializer.data)
    except NPCEvent.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
