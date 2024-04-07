"""View Module for handling requests for a townie"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Townie
from sdvapi.serializers import TownieSerializer

class TownieView(ViewSet):
  """SDVCompanion Townie View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single townie
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      townie = Townie.objects.get(pk=pk)
      serializer = TownieSerializer(townie)
      return(serializer.data)
    except Townie.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request, pk):
    """Handles GET request for all Townies
    
    Returns -> JSON serialized response -- 200 status"""
    
    townies = Townie.objects.all()
    serializer = TownieSerializer(townies, many=True)
    return Response(serializer.data)
