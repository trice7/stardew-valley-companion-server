"""View Module for handling requests for items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Item
from sdvapi.serializers import ItemSerializer

class ItemView(ViewSet):
  """SDVCompanion Item View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single item
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      item = Item.objects.get(pk=pk)
      serializer = ItemSerializer(item)
      return(serializer.data)
    except Item.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request, pk):
    """Handles GET requests for all items
    
    Returns -> JSON Serialized response -- 200 status"""
    
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
