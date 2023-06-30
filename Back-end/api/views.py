from datetime import date, timedelta
from django.shortcuts import render
from rest_framework import generics, status
from .serializers import DriverSerializer,CreateDriverSerializer, CreateTaxiDetailSerializer,ReceivedSerializer, CompletedRideSerializer, EarningsSerializer, OngoingRideSerializer, CancelledRideSerializer, CreateNewRideSerializer, DriverDashboardSerializer, AdminDashboardSerializer
#from .models import Driver, Ride
from .models import NewDriver, TaxiDetail,NewRideDetail,Earning
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .ride_service import assign_driver_to_ride

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# from rest_framework_simplejwt.authentication import JWTAuthentication

# def your_view(request):
#     # Get the Authorization header from the request
#     auth_header = request.headers.get('Authorization')

#     if auth_header:
#         # Split the header value into the authentication scheme and the token
#         auth_scheme, token = auth_header.split(' ')

#         if auth_scheme.lower() == 'bearer':
#             # Token is the JWT access token
#             jwt_access_token = token

#             # You can then use the JWT access token as needed
#             # For example, you can decode and verify the token using the JWTAuthentication class
#             authentication = JWTAuthentication()

#             try:
#                 validated_token = authentication.get_validated_token(jwt_access_token)
#                 http_driver_id= validated_token['driver_id']
#                 print(http_driver_id)
#                 return http_driver_id

#                 # Access token is valid
#                 # You can access the token claims or user details if needed
#                 # validated_token['username'], validated_token['driver_id'], etc.
#             except:
#                 # Access token is invalid or expired
#                 # Handle the error accordingly
#                 pass


import jwt
from django.conf import settings
from django.http import JsonResponse, Http404


def get_driver_id(request):
    # Get the token from the Authorization header
    auth_header = request.headers.get('Authorization')
    if auth_header:
        # Extract the token from the header (e.g., "Bearer <token>")
        token = auth_header.split(' ')[1]

        try:
            # Verify and decode the token using your secret key
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # Access the claims or data from the payload
            driver_id = payload['driver_id']
            return driver_id
            # ... Your code here ...

            # Return a JSON response or perform other actions
            # return JsonResponse({'message': 'Token verified and processed successfully.'})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired.'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token.'}, status=401)
    else:
        return JsonResponse({'error': 'Authorization header not found.'}, status=401)


# Create your views here.


#Create your views here.


# class DriverView(generics.ListAPIView):
#     queryset = NewDriver.objects.all()
#     serializer_class = DriverSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAllViewDriver(request):
    drivers = NewDriver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getViewDriver(request):

    driver_id_view_driver = get_driver_id(request)
    drivers = NewDriver.objects.filter(driver_id=driver_id_view_driver).first()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


# class CreateDriverView(generics.CreateAPIView):
#     queryset = NewDriver.objects.all()
#     serializer_class = CreateDriverSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateDriverView(request):
    driver_id = get_driver_id(request)  # Fetch the driver_id from the request
    
    serializer = CreateDriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver_id=driver_id)  # Pass the driver_id to the serializer's save method
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def updatedriverdetails(request, driver_id):
    try:
        driver = NewDriver.objects.get(driver_id=driver_id)
    except NewDriver.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = CreateDriverSerializer(driver)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreateDriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_driver(request, driver_id):
    try:
        driver = NewDriver.objects.get(driver_id=driver_id)
    except NewDriver.DoesNotExist:
        raise Http404

    driver.delete()

    return Response({'message': 'Driver deleted successfully'})

# class CreateTaxiView(generics.CreateAPIView):
#     queryset = TaxiDetail.objects.all()
#     serializer_class = CreateTaxiDetailSerializer



@api_view(['POST'])
def CreateTaxiView(request):
    driver_id_create_taxi = get_driver_id(request)
    #print(driver_id_create_taxi)

    try:
        driver = NewDriver.objects.get(pk=driver_id_create_taxi)
    except NewDriver.DoesNotExist:
        raise Http404('Driver not found.')

    request.data['driver_id'] = driver.driver_id
    print(request.data)
    serializer = CreateTaxiDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



# class TaxiView(generics.ListAPIView):
#     queryset = TaxiDetail.objects.all()
#     serializer_class = CreateTaxiDetailSerializer


# BOTH VIEW TAXI IS WORKING CORRECTLY 

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getViewAllTaxiDetails(request):
    taxi = TaxiDetail.objects.all()
    serailizer = CreateTaxiDetailSerializer(taxi, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getViewTaxiDetails(request):
    driver_id_view_taxi = get_driver_id(request)

    taxi = TaxiDetail.objects.filter(driver_id = driver_id_view_taxi).first()
    serailizer = CreateTaxiDetailSerializer(taxi)
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


# class ReceivedView(generics.ListAPIView):
#     queryset = NewRideDetail.objects.all()
#     serializer_class = ReceivedSerializer


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getViewReceived(request):
#     driver_id_received = get_driver_id(request)
#     driver= NewDriver.objects.get(driver_id = driver_id_received)
    
#     received = NewRideDetail.objects.all()
#     serailizer = ReceivedSerializer(received, many=True)
    
    
        
#     return Response(serailizer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getViewSingleReceived(request):
    driver_id_received = get_driver_id(request)
    driver = NewDriver.objects.get(driver_id=driver_id_received)
    
    received = NewRideDetail.objects.filter(driver_id = driver_id_received)
    serialized_data = []

    for ride in received:
        serialized_ride = ReceivedSerializer(ride).data
        serialized_ride['driver_name'] = driver.driver_name
        serialized_data.append(serialized_ride)

    return Response(serialized_data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getViewAllReceived(request):
    #driver_id_all_received = get_driver_id(request)
    #driver = NewDriver.objects.get(driver_id=driver_id_all_received)
    
    received = NewRideDetail.objects.all()
    
    serialized_data = []

    for ride in received:
        driver = NewDriver.objects.get(driver_id = ride.driver_id.driver_id)
        serialized_ride = ReceivedSerializer(ride).data
        serialized_ride['driver_name'] = driver.driver_name
        serialized_data.append(serialized_ride)

    return Response(serialized_data)
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



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllViewCompleted(request):
    completed = NewRideDetail.objects.filter(status='completed')
    serailizer = CompletedRideSerializer(completed, many=True)
    return Response(serailizer.data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getViewCompleted(request):
    driver_id_view_completed = get_driver_id(request)
    completed = NewRideDetail.objects.filter(driver_id = driver_id_view_completed, status='completed')
    serailizer = CompletedRideSerializer(completed, many=True)
    return Response(serailizer.data)


# class ReceivedRideDetailsView(APIView):
#     serializer_class = ReceivedSerializer

#     def get(self, request, rideId):
#         try:
#             ride = NewRideDetail.objects.get(rideId=rideId)
#             user_name = ride.user_name
#             start_from = ride.start_from
#             destination = ride.destination
#             reachedtime = ride.reachedtime
#             _status = ride.status
#             return Response(
#                 {'rideId': rideId, 'user_name': user_name, 'start_from': start_from, 'destination': destination,
#                  'reachedtime': reachedtime, 'status': _status})
#         except NewRideDetail.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def received_ride_details_view(request, rideId):
    try:
        ride = NewRideDetail.objects.get(rideId=rideId)
        driver = NewDriver.objects.get(driver_id = ride.driver_id.driver_id)
        driver_name = driver.driver_name
        passenger_name = ride.passenger_name
        start_from = ride.start_from
        destination = ride.destination
        reachedtime = ride.reachedtime
        _status = ride.status
        return Response({
            #'rideId': rideId,
            'passenger_name':passenger_name ,
            'driver_name': driver_name,
            'start_from': start_from,
            'destination': destination,
            'reachedtime': reachedtime,
            'status': _status
        })
    except NewRideDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# class CancelledRideView(generics.ListAPIView):
#     queryset = NewRideDetail.objects.filter(status='cancelled')
#     serializer_class = CancelledRideSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllViewCancelled(request):
    cancelled = NewRideDetail.objects.filter(status='cancelled')
    serailizer = CancelledRideSerializer(cancelled, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getViewCancelled(request):
    driver_id_view_cancelled = get_driver_id(request)
    cancelled = NewRideDetail.objects.filter(driver_id = driver_id_view_cancelled,status='cancelled')
    serailizer = CancelledRideSerializer(cancelled, many=True)
    return Response(serailizer.data)


# class CancelledRideDetailsView(APIView):
#     serializer_class = CancelledRideSerializer

#     def get(self, request, rideId):
#         try:
#             ride = NewRideDetail.objects.get(rideId=rideId)
#             user_name = ride.user_name
#             start_from = ride.start_from
#             destination = ride.destination
#             _status = ride.status
#             return Response(
#                 {'rideId': rideId, 'user_name': user_name, 'start_from': start_from, 'destination': destination,
#                  'status': _status})
#         except NewRideDetail.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class CreateNewRideView(generics.CreateAPIView):
#     queryset = NewDriver.objects.all()
#     serializer_class = CreateNewRideSerializer

# @api_view(['POST'])
# def CreateNewRideView(request):
#     serializer = CreateNewRideSerializer(data=request.data)
#     if serializer.is_valid():
#         new_ride = serializer.save()

       
#         # Retrieve the rideId from the created instance
#         ride_id = new_ride.rideId
        
#         # Call assign_driver_to_ride(ride_id) method here
#         assign_driver_to_ride(ride_id)

#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)




@api_view(['POST'])
def CreateNewRideView(request):
    serializer = CreateNewRideSerializer(data=request.data)
    if serializer.is_valid():
        ac = serializer.save()
        # print(serializer.validated_data)
        # print(
        # ride_id = serializer.validated_data['rideId']
        
        ride_id = ac.rideId
        #print(ride_id)
        ass_dri = assign_driver_to_ride(ride_id)
        ac.driver_id = ass_dri
        serializer.save()

        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Earnings_of_single_driver(request):
    try:
        driver_id_view_single_earnings = get_driver_id(request)
        driver = NewDriver.objects.get(driver_id = driver_id_view_single_earnings)
        driver_name = driver.driver_name

        earnings = Earning.objects.get(driver_id=driver_id_view_single_earnings)
        total_earnings = earnings.total_earnings
        total_rides = earnings.total_rides
        total_pending = earnings.total_pending
        total_paid = earnings.total_paid
        
        return Response({
                    'driver_id': driver_id_view_single_earnings,
                    'driver_name': driver_name,
                    'total_earnings': total_earnings,
                    'total_rides': total_rides,
                    'total_pending': total_pending,
                    'total_paid': total_paid
                })
    except NewDriver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
#@permission_classes([IsAdminUser])
def Earnings_of_all_drivers(request):
    try:
        drivers = NewDriver.objects.all()

        earnings_data = []
        for driver in drivers:
            driver_id = driver.driver_id
            driver_name = driver.driver_name

            earnings = Earning.objects.get(driver_id=driver_id)
            total_earnings = earnings.total_earnings
            total_rides = earnings.total_rides
            total_pending = earnings.total_pending
            total_paid = earnings.total_paid

            earnings_data.append({
                'driver_id': driver_id,
                'driver_name': driver_name,
                'total_earnings': total_earnings,
                'total_rides': total_rides,
                'total_pending': total_pending,
                'total_paid': total_paid
            })

        return Response(earnings_data)
    except (NewDriver.DoesNotExist, Earning.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)




# class EarningsView(APIView):
#     serializer_class = EarningsSerializer

#     def get(self, request, driver_id):
#         try:
#             driver = NewDriver.objects.get(driver_id=driver_id)
#             driver_name = driver.driver_name

#             # Retrieve earnings data from Earnings model
#             earnings = Earning.objects.get(driver_id=driver_id)
#             total_earnings = earnings.total_earnings
#             total_rides = earnings.total_rides
#             total_pending = earnings.total_pending
#             total_paid = earnings.total_paid

#             return Response({
#                 'driver_id': driver_id,
#                 'driver_name': driver_name,
#                 'total_earnings': total_earnings,
#                 'total_rides': total_rides,
#                 'total_pending': total_pending,
#                 'total_paid': total_paid
#             })
#         except NewDriver.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)



    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getViewOngoing(request):
    ongoing = NewRideDetail.objects.filter(status='ongoing')
    serailizer = OngoingRideSerializer(ongoing, many=True)
    return Response(serailizer.data)

@api_view(['GET'])
# permission_classes([IsAuthenticated])
def getAllViewOngoing(request):
    driver_id_view_ongoing = get_driver_id(request)
    ongoing = NewRideDetail.objects.filter(driver_id = driver_id_view_ongoing,status='ongoing')
    serailizer = OngoingRideSerializer(ongoing,many = True)
    return Response(serailizer.data)





@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAdminViewDashboard(request):
    # Calculate the date range for the previous three days
    today = date.today()
    three_days_ago = today - timedelta(days=3)

    # Initialize dictionaries to store driver information and daily totals
    driver_data = {}
    daily_totals = {}

    # Iterate over each driver
    drivers = NewDriver.objects.all()
    for driver in drivers:
        driver_id = driver.driver_id

        # Calculate the total rides and earnings for the driver
        rides = NewRideDetail.objects.filter(driver_id=driver_id)
        total_rides = rides.count()
        total_earnings = sum(ride.expectedDriverPay or 0 for ride in rides)

        # Store the driver information in the dictionary
        driver_data[driver_id] = {
            'driver_id': driver_id,
            'driver_name': driver.driver_name,
            'total_rides': total_rides,
            'total_earnings': total_earnings
        }

        # Calculate the total rides and earnings for each day in the date range
        current_date = three_days_ago
        while current_date <= today:
            rides_per_day = rides.filter(requested_time__date=current_date)

            # Calculate total rides and earnings for the current day
            total_rides_per_day = rides_per_day.count()
            total_earnings_per_day = sum(ride.expectedDriverPay or 0 for ride in rides_per_day)

            # Store the daily totals in the dictionary
            if current_date.strftime('%Y-%m-%d') not in daily_totals:
                daily_totals[current_date.strftime('%Y-%m-%d')] = {
                    'total_rides': 0,
                    'total_earnings': 0
                }
            daily_totals[current_date.strftime('%Y-%m-%d')]['total_rides'] += total_rides_per_day
            daily_totals[current_date.strftime('%Y-%m-%d')]['total_earnings'] += total_earnings_per_day

            current_date += timedelta(days=1)

    # Find the day with the highest number of rides
    max_rides_day = max(daily_totals, key=lambda k: daily_totals[k]['total_rides'])

    # Add the day with the highest number of rides to the dashboard data
    dashboard_data = {
        'drivers': driver_data,
        'daily_totals': daily_totals,
        'max_rides_day': max_rides_day
    }

    serializer = AdminDashboardSerializer(dashboard_data)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDriverViewDashboard(request):
    driver_id_dashboard = get_driver_id(request)

    # Calculate the date range for the previous three days
    today = date.today()
    three_days_ago = today - timedelta(days=3)

    # Initialize a dictionary to store daily totals
    daily_totals = []

    # Calculate the total rides and earnings for each day in the date range
    current_date = three_days_ago
    while current_date <= today:
        
        rides = NewRideDetail.objects.filter(driver_id=driver_id_dashboard, requested_time__date=current_date)
        print(rides)
        print(current_date)
        # Calculate total rides and earnings for the current day
        total_rides = rides.count()
        total_earnings = sum(ride.expectedDriverPay or 0 for ride in rides)

        # Store the daily totals in the dictionary
        daily_total = {
            'date': current_date.strftime('%Y-%m-%d'),
            'total_rides': total_rides,
            'total_earnings': total_earnings
        }

        daily_totals.append(daily_total)

        current_date += timedelta(days=1)

    # Retrieve the driver's information from NewDriver model
    driver = NewDriver.objects.get(driver_id=driver_id_dashboard)

    # Create the dashboard data dictionary
    dashboard_data = {
        'driver_id': driver.driver_id,
        'driver_name': driver.driver_name,
        'total_rides': sum(totals['total_rides'] for totals in daily_totals),
        'total_earnings': sum(totals['total_earnings'] for totals in daily_totals),
        'daily_totals': daily_totals
    }

    serializer = DriverDashboardSerializer(dashboard_data)
    return Response(serializer.data)




@api_view(['PUT'])
def update_ride_status(request, ride_id):
    ride = get_object_or_404(NewRideDetail, rideId=ride_id)

    if request.method == 'POST':
        status = request.POST.get('status')

        # Update the status of the ride
        ride.status = status
        ride.save()

        return JsonResponse({'message': 'Ride status updated successfully.'})

    return JsonResponse({'message': 'Invalid request method.'}, status=400)

@api_view(['PUT'])
def update_driver_status(request, driver_id):
    driver = get_object_or_404(NewDriver, driver_id=driver_id)

    if request.method == 'POST':
        status = request.POST.get('status')

        # Update the status of the driver
        driver.driver_status = status
        driver.save()

        return JsonResponse({'message': 'Driver status updated successfully.'})

    return JsonResponse({'message': 'Invalid request method.'}, status=400)


@api_view(['PUT'])
def change_driver_availability(request, driver_id):
    driver = get_object_or_404(NewDriver, driver_id=driver_id)

    if request.method == 'POST':
        is_available = request.POST.get('is_available')

        # Update the availability status of the driver
        driver.driver_status = 'available' if is_available == 'true' else 'unavailable'
        driver.save()

        return JsonResponse({'message': 'Driver availability status updated successfully.'})

    return JsonResponse({'message': 'Invalid request method.'}, status=400)



@api_view(['POST'])
def delete_or_disable_driver(request, driver_id):
    driver = get_object_or_404(NewDriver, driver_id=driver_id)

    if request.method == 'POST':
        # Check if the driver is involved in any ongoing rides
        ongoing_rides = NewRideDetail.objects.filter(driver_id=driver, status__in=['requested', 'accepted'])
        if ongoing_rides.exists():
            return JsonResponse({'message': 'Driver cannot be deleted or disabled while involved in ongoing rides.'}, status=400)

        # Delete or disable the driver based on the action specified
        action = request.POST.get('action')
        if action == 'delete':
            driver.delete()
            return JsonResponse({'message': 'Driver deleted successfully.'})
        elif action == 'disable':
            driver.driver_status = 'disabled'
            driver.save()
            return JsonResponse({'message': 'Driver disabled successfully.'})
        else:
            return JsonResponse({'message': 'Invalid action specified.'}, status=400)

    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_all_drivers(request):
    drivers = NewDriver.objects.all()
    drivers_data = []

    for driver in drivers:
        taxi = TaxiDetail.objects.get(driver_id=driver)
        driver_data = {
            'driver_id': driver.driver_id,
            'driver_name': driver.driver_name,
            'driver_email': driver.driver_email,
            'taxi_num': taxi.taxi_num,
            'taxi_test_date': taxi.taxi_test_date,
            'taxi_pollution_validity': taxi.taxi_pollution_validity,
            'taxi_insurance': taxi.taxi_insurance,
            'taxi_type': taxi.taxi_type,
            'taxi_manufacturer': taxi.taxi_manufacturer,
            'taxi_model': taxi.taxi_model,
        }
        drivers_data.append(driver_data)

    return JsonResponse({'drivers': drivers_data})


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