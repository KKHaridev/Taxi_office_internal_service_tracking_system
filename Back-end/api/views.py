from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer, CreateDriverSerializer, ReceivedSerializer, CompletedRideSerializer, EarningsSerializer, OngoingRideSerializer
from .models import Driver, Ride
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
            #queryset = Driver.objects.filter(driver_id=driver_id)


class ReceivedView(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = ReceivedSerializer


'''class CreateNewReqView(APIView):
    serializer_class = ReceivedSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_name = serializer.data.user_name
            start_from = serializer.data.start_from
            destination = serializer.data.destination
            status = serializer.data.status'''


class CompletedRideView(generics.ListAPIView):
    queryset = Ride.objects.filter(status='Completed')
    serializer_class = CompletedRideSerializer


class EarningsView(APIView):
    serializer_class = EarningsSerializer

    def get(self, request, driver_id):
        try:
            driver = Driver.objects.get(driver_id=driver_id)
            earnings = driver.total_earnings
            return Response({'earnings': earnings})
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OngoingRideView(generics.ListAPIView):
    serializer_class = OngoingRideSerializer

    def get_queryset(self):
        return Ride.objects.filter(status='ongoing')


# Driver login
# Dashboard
# Received
# New ride
# Driver sign up
# Driver profile
# Completed ride
# 		->details
# Ongoing ride
# Earnings
# Canceled


# Admin login
# Dashboard
# Profile
# Received requests
# 		-> details
# Cars and Drivers
# Earnings
# Canceled
# Completed
# 		-> details
