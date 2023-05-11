from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        driver_id = ''.join(random.choices(string.digits, k=length))
        if Driver.objects.filter(driver_id=driver_id).count() == 0:
            break

    return driver_id


# Create your models here.
class Driver(models.Model):
    driver_id = models.CharField(
        max_length=10, default=generate_unique_code, unique=True)
    driver_name = models.CharField(max_length=30, default="", unique=False)
    driver_email = models.CharField(max_length=50)
    taxi_num = models.CharField(max_length=10, unique=True)
    driver_phone = models.CharField(max_length=11)
    taxi_test_date = models.DateField(
        auto_now=False, auto_now_add=False, max_length=12)
    taxi_pollution_validity = models.DateField(
        auto_now=False, auto_now_add=False, max_length=12)
    taxi_insurance = models.DateField(
        auto_now=False, auto_now_add=False, max_length=12)
    taxi_type = models.CharField(max_length=10, default='')
    taxi_model = models.CharField(max_length=10, default='')
    driver_status = models.CharField(max_length=10, default="available")
    driver_upi = models.CharField(max_length=10, default='', unique=True)
    total_earnings = models.IntegerField(default=0)
    total_rides = models.IntegerField(default=0)
    total_paid = models.IntegerField(default=0)
    total_pending = models.IntegerField(default=0)


class Ride(models.Model):
    rideId = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=250)
    start_from = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    requested_time = models.DateTimeField(auto_now_add=True)
    starting_time = models.DateTimeField(auto_now_add=False)
    reachedtime = models.DateTimeField(auto_now_add=False)
    expectedReachingtime = models.TimeField(auto_now_add=False)
    status = models.CharField(max_length=20)
    carpool = models.BooleanField(default=False)
    expectedDriverPay = models.CharField(max_length=7)
    carpoolPercent = models.IntegerField(max_length=3, default=0)

