"""View Module for handling requests for a shop"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Shop
from sdvapi.serializers import ShopSerializer

class ShopView(ViewSet):
  """SDVCompanion Shop View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single Shop
    
    Returns -> JSON serialized response -- 200 status"""
    
    try:
      shop = Shop.objects.get(pk=pk)
      serializer = ShopSerializer(shop)
      return(serializer.data)
    except Shop.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request, pk):
    """Handles GET request for all Shops
    
    Returns -> JSON serialized response -- 200 status"""
    
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)
