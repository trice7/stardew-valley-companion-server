"""View moadule for handling requests for a bundle"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Bundle, CenterRoom
from sdvapi.serializers import BundleSerializer

class BundleView(ViewSet):
  """SDVCompanion Bundle View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single bundle
    
    Returns -> JSON serialized response -- status 200"""
    
    try:
      bundle = Bundle.objects.get(pk=pk)
      serializer = BundleSerializer(bundle)
      return Response(serializer.data)
    except Bundle.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET requests for all bundles
    
    Returns -> JSON serialized list of responses -- status 200"""
    
    bundles = Bundle.objects.all()
    serializer = BundleSerializer(serializer, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handles POST requests for a bundle
    
    Returns -> JSON serialized response -- status 201"""
    
    center_room = CenterRoom.objects.get(pk=request.data['centerRoom'])
    
    bundle = Bundle.objects.create(
      name = request.data['name'],
      image = request.data['imageUrl'],
      room = center_room,
      items_needed = request.data['itemsNeeded'],
      reward = request.data['reward'],
      reward_amount = request.data['rewardAmount']
    )
    
    serializer = BundleSerializer(bundle)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a bundle
    
    Returns -> JSON serialized response -- status 200"""
    
    bundle = Bundle.objects.get(pk=pk)
    center_room = CenterRoom.objects.get(pk=request.data['centerRoom'])
    
    bundle.name = request.data['name']
    bundle.image = request.data['imageUrl']
    room = center_room
    items_needed = request.data['itemsNeeded']
    reward = request.data['reward']
    reward_amount = request.data['rewardAmount']
    
    bundle.save()
    serializer = BundleSerializer(bundle)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, pk):
    """Handels DELETE requests for a bundle
    
    Returns -> Empty body -- 204 status"""
    
    bundle = Bundle.objects.get(pk=pk)
    bundle.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
