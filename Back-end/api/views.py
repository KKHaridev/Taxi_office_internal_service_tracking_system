from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer, CreateDriverSerializer
from .models import Driver
from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.

class DriverView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class CreateDriverView(APIView):
    serializer_class = CreateDriverSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            driver_name = serializer.data.driver_name
            driver_email = serializer.data.driver_email
            taxi_num = serializer.data.taxi_num
            queryset = Driver.objects.filter(driver_id=driver_id)
