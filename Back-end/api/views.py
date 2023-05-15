from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer, CreateDriverSerializer, ReceivedSerializer, CompletedRideSerializer, EarningsSerializer, OngoingRideSerializer, CancelledRideSerializer, CreateNewRideSerializer
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
            queryset = Driver.objects.all()


class ReceivedView(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = ReceivedSerializer


'''class CreateNewReqView(APIView):
    serializer_class = CreateNewRideSerializer

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
    queryset = Ride.objects.filter(status='completed')
    serializer_class = CompletedRideSerializer

class CompletedRideDetailsView(APIView):
    serializer_class = CompletedRideSerializer

    def get(self, request, rideId):
        try:
            ride = Ride.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            reachedtime = ride.reachedtime
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination,'reachedtime':reachedtime, 'status':_status})
        except Ride.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class CancelledRideView(generics.ListAPIView):
    queryset = Ride.objects.filter(status='cancelled')
    serializer_class = CancelledRideSerializer

class CancelledRideDetailsView(APIView):
    serializer_class = CancelledRideSerializer

    def get(self, request, rideId):
        try:
            ride = Ride.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination, 'status':_status})
        except Ride.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateNewRideView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = CreateNewRideSerializer

class EarningsView(APIView):
    serializer_class = EarningsSerializer

    def get(self, request, driver_id):
        try:
            driver = Driver.objects.get(driver_id=driver_id)
            earnings = driver.total_earnings
            total_rides = driver.total_rides
            total_pending = driver.total_pending
            total_paid = driver.total_paid
            return Response({'earnings': earnings,'total_rides':total_rides,'total_pending':total_pending,'total_paid':total_paid })
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OngoingRideView(generics.ListAPIView):
    serializer_class = OngoingRideSerializer

    def get_queryset(self):
        return Ride.objects.filter(status='ongoing')


# Dashboard

# New ride
# Driver sign up
# Driver profile



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
