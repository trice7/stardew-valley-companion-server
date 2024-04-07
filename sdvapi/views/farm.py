"""View Module for handling requests for farms"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Farm, Player
from sdvapi.serializers import FarmSerializer

class FarmView(ViewSet):
  """SDVCompanion Farm View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single Farm
    
    Returns -> JSON serialized response for a single farm -- 200 status"""
    
    try:
      farm = Farm.objects.get(pk=pk)
      serializer = FarmSerializer(farm)
      return Response(serializer.data)
    except Farm.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request, pk):
    """Handles GET requests for a list of farms
    
    Returns -> JSON serialized list of farms -- 200 status"""
    
    farms = Farm.objects.all()
    
    # Code below will check to see if a GET all request queries a uid
    # If True, it will change the value of farms to only include that users farms, otherwise it will return all farms
    uid = request.query_params.get('uid')
    if uid is not None:
      player = Player.objects.get(uid=uid)
      farms = Farm.objects.filter(owner=player.id)
    # ------------------------------------------------
    
    serializer = FarmSerializer(farms, many=True)
    return Response(serializer.data)
  
  def create(self, request, pk):
    """Handles POST requests for a farm
    
    Returns -> JSON serialized response -- 201 status"""
    
    player = Player.objects.get(uid=request.data['uid'])
    
    farm = Farm.objects.create(
      owner = player,
      name = request.data['name']
    )
    
    serializer = FarmSerializer(farm)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a farm
    
    Returns -> JSON serialized response -- 200 status"""
    
    player = Player.objects.get(uid=request.data['uid'])
    farm = Farm.objects.get(pk=pk)
    
    farm.owner = player
    farm.name = request.data['name']
    
    farm.save()
    serializer = FarmSerializer(farm)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE requests for a farm
    
    Returns -> Empty body -- 204 status"""
    
    farm = Farm.objects.get(pk=pk)
    farm.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
