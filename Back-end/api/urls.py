from django.urls import include, path
from .views import DriverView

urlpatterns = [
    path('home',DriverView.as_view()),
]