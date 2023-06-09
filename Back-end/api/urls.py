from django.urls import include, path
from . import views
urlpatterns = [
    path('viewdriver', views.DriverView.as_view()),
    path('createdriver', views.CreateDriverView.as_view()),
    path('viewtaxi',views.TaxiView.as_view()),
    path('createtaxi',views.CreateTaxiView.as_view()),
    path('received', views.ReceivedView.as_view()),
    path('completedrides', views.CompletedRideView.as_view()),
    path('completedrides/<str:rideId>/', views.CompletedRideDetailsView.as_view()),
    path('cancelledrides', views.CancelledRideView.as_view()),
    path('cancelledrides/<str:rideId>/',views.CancelledRideDetailsView.as_view()),
    path('<str:driver_id>/earnings', views.EarningsView.as_view()),
    path('ongoingrides', views.OngoingRideView.as_view()),
    path('createnewride',views.CreateNewRideView.as_view()),
    path('dashboard',views.DriverDashboardView.as_view()),
    

]


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

'''from django.urls import path
from .views import (
    DriverView,
    DriverDetailView,
    PassengerView,
    PassengerDetailView,
    RideView,
    RideDetailView,
    EarningsView,
    OngoingRideView,
)

urlpatterns = [
    path('drivers/', DriverView.as_view(), name='driver_list'),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver_detail'),
    #path('passengers/', PassengerView.as_view(), name='passenger_list'),
    #path('passengers/<int:pk>/', PassengerDetailView.as_view(), name='passenger_detail'),
    path('rides/', RideView.as_view(), name='ride_list'),
    path('rides/<int:pk>/', RideDetailView.as_view(), name='ride_detail'),
    path('earnings/', EarningsView.as_view(), name='earnings_list'),
    path('ongoing-rides/', OngoingRideView.as_view(), name='ongoing_rides_list'),
]
'''
