from django.urls import include, path
from .views import DriverView, ReceivedView

urlpatterns = [
    path('home', DriverView.as_view()),
    path('recreq', ReceivedView.as_view()),
    # path('completedride',),
    # path('earnings',),
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