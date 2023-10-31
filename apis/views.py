from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from store.models import Plant
from .serializers import PlantSerializer

class PlantAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

