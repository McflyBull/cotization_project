from django.shortcuts import render

import json

# Create your views here.

from rest_framework import viewsets

from cotization_api.serializers import DollarSerializer

from cotization_api.models import dollar



class DollarViewSet(viewsets.ModelViewSet):

   queryset = dollar.objects.all()

   serializer_class = DollarSerializer