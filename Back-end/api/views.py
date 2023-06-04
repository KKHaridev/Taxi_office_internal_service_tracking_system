from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer,CreateDriverSerializer, CreateTaxiDetailSerializer,ReceivedSerializer, CompletedRideSerializer, EarningsSerializer, OngoingRideSerializer, CancelledRideSerializer, CreateNewRideSerializer, DriverDashboardSerializer
#from .models import Driver, Ride
from .models import NewDriver, TaxiDetails,NewRideDetails,Earnings
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class DriverView(generics.ListAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = DriverSerializer

    
class CreateDriverView(generics.CreateAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = CreateDriverSerializer

class CreateTaxiView(generics.CreateAPIView):
    queryset = TaxiDetails.objects.all()
    serializer_class = CreateTaxiDetailSerializer

class TaxiView(generics.ListAPIView):
    queryset = TaxiDetails.objects.all()
    serializer_class = CreateTaxiDetailSerializer

# class CreateDriverView(APIView):
#     serializer_class = CreateDriverSerializer

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             driver_name = serializer.data.driver_name
#             driver_email = serializer.data.driver_email
#             taxi_num = serializer.data.taxi_num
#             #queryset = Driver.objects.filter(driver_id=driver_id)
#             queryset = Driver.objects.all()


class ReceivedView(generics.ListAPIView):
    queryset = NewRideDetails.objects.all()
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
    queryset = NewRideDetails.objects.filter(status='completed')
    serializer_class = CompletedRideSerializer

class CompletedRideDetailsView(APIView):
    serializer_class = CompletedRideSerializer

    def get(self, request, rideId):
        try:
            ride = NewRideDetails.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            reachedtime = ride.reachedtime
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination,'reachedtime':reachedtime, 'status':_status})
        except NewRideDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class CancelledRideView(generics.ListAPIView):
    queryset = NewRideDetails.objects.filter(status='cancelled')
    serializer_class = CancelledRideSerializer

class CancelledRideDetailsView(APIView):
    serializer_class = CancelledRideSerializer

    def get(self, request, rideId):
        try:
            ride = NewRideDetails.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination, 'status':_status})
        except NewRideDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateNewRideView(generics.CreateAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = CreateNewRideSerializer

class EarningsView(APIView):
    serializer_class = EarningsSerializer

    def get(self, request, driver_id):
        try:
            driver = Earnings.objects.get(driver_id=driver_id)
            earnings = driver.total_earnings
            total_rides = driver.total_rides
            total_pending = driver.total_pending
            total_paid = driver.total_paid
            return Response({'earnings': earnings,'total_rides':total_rides,'total_pending':total_pending,'total_paid':total_paid })
        except NewDriver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OngoingRideView(generics.ListAPIView):
    serializer_class = OngoingRideSerializer

    def get_queryset(self):
        return NewRideDetails.objects.filter(status='ongoing')
    

class DriverDashboardView(generics.ListAPIView):
    serializer_class = DriverDashboardSerializer

    def get_queryset(self):
        return NewDriver.objects.all()


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
