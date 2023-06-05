from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer,CreateDriverSerializer, CreateTaxiDetailSerializer,ReceivedSerializer, CompletedRideSerializer, EarningsSerializer, OngoingRideSerializer, CancelledRideSerializer, CreateNewRideSerializer, DriverDashboardSerializer
#from .models import Driver, Ride
from .models import NewDriver, TaxiDetail,NewRideDetail,Earning
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


class DriverView(generics.ListAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = DriverSerializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewDriver(request):
    drivers = NewDriver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)
    
class CreateDriverView(generics.CreateAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = CreateDriverSerializer

class CreateTaxiView(generics.CreateAPIView):
    queryset = TaxiDetail.objects.all()
    serializer_class = CreateTaxiDetailSerializer

class TaxiView(generics.ListAPIView):
    queryset = TaxiDetail.objects.all()
    serializer_class = CreateTaxiDetailSerializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewTaxiDetails(request):
    taxi = TaxiDetail.objects.all()
    serailizer = CreateTaxiDetailSerializer(taxi, many=True)
    return Response(serailizer.data)

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
    queryset = NewRideDetail.objects.all()
    serializer_class = ReceivedSerializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewReceived(request):
    received = NewRideDetail.objects.all()
    serailizer = ReceivedSerializer(received, many = True)
    return Response(serailizer.data)

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
    queryset = NewRideDetail.objects.filter(status='completed')
    serializer_class = CompletedRideSerializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewCompleted(request):
    completed = NewRideDetail.objects.filter(status='completed')
    serailizer = CompletedRideSerializer(completed, many = True)
    return Response(serailizer.data)

class CompletedRideDetailsView(APIView):
    serializer_class = CompletedRideSerializer

    def get(self, request, rideId):
        try:
            ride = NewRideDetail.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            reachedtime = ride.reachedtime
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination,'reachedtime':reachedtime, 'status':_status})
        except NewRideDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class CancelledRideView(generics.ListAPIView):
    queryset = NewRideDetail.objects.filter(status='cancelled')
    serializer_class = CancelledRideSerializer


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewCancelled(request):
    cancelled = NewRideDetail.objects.filter(status='cancelled')
    serailizer = CancelledRideSerializer(cancelled, many = True)
    return Response(serailizer.data)



class CancelledRideDetailsView(APIView):
    serializer_class = CancelledRideSerializer

    def get(self, request, rideId):
        try:
            ride = NewRideDetail.objects.get(rideId=rideId)
            user_name = ride.user_name
            start_from = ride.start_from
            destination = ride.destination
            _status = ride.status
            return Response({'rideId':rideId,'user_name': user_name,'start_from':start_from,'destination':destination, 'status':_status})
        except NewRideDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateNewRideView(generics.CreateAPIView):
    queryset = NewDriver.objects.all()
    serializer_class = CreateNewRideSerializer

class EarningsView(APIView):
    serializer_class = EarningsSerializer

    def get(self, request, driver_id):
        try:
            driver = Earning.objects.get(driver_id=driver_id)
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
        return NewRideDetail.objects.filter(status='ongoing')
    

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewOngoing(request):
    ongoing = NewRideDetail.objects.filter(status='ongoing')
    serailizer = OngoingRideSerializer(ongoing, many = True)
    return Response(serailizer.data)




class DriverDashboardView(generics.ListAPIView):
    serializer_class = DriverDashboardSerializer

    def get_queryset(self):
        return NewDriver.objects.all()


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getViewDashboard(request):
    dashboard = NewDriver.objects.all()
    serailizer = DriverDashboardSerializer(dashboard, many = True)
    return Response(serailizer.data)



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
