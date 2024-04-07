"""View Module for handling requests for a community center room"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import Farm, CenterRoom
from sdvapi.serializers import CenterRoomSerializer

class CenterRoomView(ViewSet):
  """SDVCompanion Center Room View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for a single community center room
    
    Returns -> JSON serialized response -- status 200"""
    
    try:
      center_room = CenterRoom.objects.get(pk=pk)
      serializer = CenterRoomSerializer(center_room)
      return Response(serializer.data)
    except CenterRoom.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, reqeust):
    """Handles GET requests for all community center rooms
    
    Returns -> JSON serialized list response -- status 200"""
    
    center_rooms = CenterRoom.objects.all()
    serializer = CenterRoomSerializer(center_rooms, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handles POST requests for a community center room
    
    Returns -> JSON serialized response -- status 201"""
    
    farm = Farm.objects.get(pk=request.data['save'])
    
    center_room = CenterRoom.objects.create(
      name = request.data['name'],
      reward = request.data['reward'],
      save = farm
    )

    serializer = CenterRoomSerializer(center_room)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for a community center room
    
    Returns -> JSON serialized response -- 200 status"""
    
    farm = Farm.objects.get(pk=request.data['save'])
    center_room = CenterRoom.objects.get(pk=pk)
    
    center_room.name = request.data['name']
    center_room.reward = request.data['reward']
    center_room.save = farm
    
    center_room.save()
    serializer = CenterRoomSerializer(center_room)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a community center room
    
    Returns -> Empty body -- status 204"""
    
    center_room = CenterRoom.objects.get(pk=pk)
    center_room.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
