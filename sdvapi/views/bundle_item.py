"""View Module for handling requests for a bundles items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sdvapi.models import BundleItem, Bundle, Item

# class BundleItemView(ViewSet):
#   """SDVCompanion Bundle Item View"""
  
#   def retrieve(self, request, pk):
#     """Handles GET reqeusts for a single item
    
#     Returns -> JSON serialized response -- Status 200"""
    
#     try:
#       bundle_item = BundleItem.objects.get(pk=pk)
      