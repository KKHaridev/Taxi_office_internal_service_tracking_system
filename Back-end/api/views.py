from django.shortcuts import render
from rest_framework import generics
from .serializers import DriverSerializer
from .models import Driver

# Create your views here.

class DriverView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer