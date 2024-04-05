"""View Module for handling requests for a bundles items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import BundleItem, Bundle, Item
from sdvapi.serializers import BundleItemSerializer

class BundleItemView(ViewSet):
  """SDVCompanion Bundle Item View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single item
    
    Returns -> JSON serialized response -- Status 200"""
    
    try:
      bundle_item = BundleItem.objects.get(pk=pk)
      serializer = BundleItemSerializer(bundle_item)
      return Response(serializer.data)
    except BundleItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all bundle items
    
    Returns -> JSON serialized list -- Status 200"""
    
    bundle_items = BundleItem.objects.all()
    serializer = BundleItemSerializer(bundle_items, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handles POST requests for a bundle item
    
    Returns -> JSON serialized response -- status 201"""
    
    bundle = Bundle.objects.get(pk=request.data['bundle'])
    item = Item.objects.get(pk=request.data['item'])
    
    bundle_item = BundleItem.objects.create(
      bundle = bundle,
      item = item,
      quantity = request.data['quantity'],
      quality = request.data['quality']
    )
    
    serializer = BundleItemSerializer(bundle_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a bundle item
    
    Returns -> JSON serialized response -- status 200"""
    
    bundle = Bundle.objects.get(pk=request.data['bundle'])
    item = Item.objects.get(pk=request.data['item'])
    
    bundle_item = BundleItem.objecst.get(pk=pk)
    
    bundle_item.bundle = bundle
    bundle_item.item = item
    bundle_item.quantity = request.data['quantity']
    bundle_item.quality = request.data['quality']
    
    bundle_item.save()
    serializer = BundleItemSerializer(bundle_item)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, pk):
    """Handles DELETE requests for a bundle item
    
    Returns -> Empty body -- 204 status"""
    
    bundle_item = BundleItem.objects.get(pk=pk)
    bundle_item.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
