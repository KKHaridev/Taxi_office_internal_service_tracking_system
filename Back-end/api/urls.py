from django.urls import include, path
from .views import DriverView, ReceivedView

urlpatterns = [
    path('home', DriverView.as_view()),
    path('recreq', ReceivedView.as_view()),

]
