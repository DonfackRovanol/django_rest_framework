from django.shortcuts import render
from rest_framework import generics, mixins
from .models import entreprise
from .serializeprice import entrepriseserializes

# Create your views here.

class ListCreateList(generics.ListCreateAPIView):
    
    queryset = entreprise.objects.all()
    serializer_class = entrepriseserializes
