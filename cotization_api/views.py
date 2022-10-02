from django.shortcuts import render
import json
from rest_framework import viewsets
from cotization_api.serializers import DollarSerializer
from cotization_api.models import Dollar
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.


class DollarViewSet(viewsets.ModelViewSet):
   queryset = Dollar.objects.all()
   serializer_class = DollarSerializer
   http_method_names = ['get', 'put', 'patch', 'post', 'head', 'options', 'trace', 'delete',]

   @action(methods=["delete"], detail=False, )
   def delete(self, request:Request):
      delete_cotization = self.queryset.filter(id__in=delete_id)
      delete_cotization.delete()
      return Response( self.serializer_class(delete_cotization,many=True).data) 