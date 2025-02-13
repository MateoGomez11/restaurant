from django.shortcuts import render
from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer  

class ViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
