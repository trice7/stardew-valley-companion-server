"""View Module for handling requests for item types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import ItemType
from sdvapi.serializers import ItemTypeSerializer

class ItemTypeView(ViewSet):
  """SDVCompanion Item Type View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single item type
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      item_type = ItemType.objects.get(pk=pk)
      serializer = ItemTypeSerializer(item_type)
      return Response(serializer.data)
    except ItemType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, reqeust, pk):
    """Handles GET requests for all item types
    
    Returns -> JSON serialized response -- 200 status"""
    
    item_types = ItemType.objects.all()
    serializer = ItemTypeSerializer(item_types, many=True)
    return Response(serializer.data)
