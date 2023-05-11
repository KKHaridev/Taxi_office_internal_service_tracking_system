from django.urls import include, path
from . import views
urlpatterns = [
    path('home', views.DriverView.as_view()),
    path('createdriver', views.CreateDriverView.as_view()),
    path('received', views.ReceivedView.as_view()),
    path('completedrides', views.CompletedRideView.as_view()),
    path('earnings/<str:driver_id>/', views.EarningsView.as_view()),
    path('ongoingrides', views.OngoingRideView.as_view()),
    # path('completedride',),done
    # path('earnings',),done
    # path('dashboard'),
    # path('cancelled'),
    # path('ongoingride'),
    # path('newride'),

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
