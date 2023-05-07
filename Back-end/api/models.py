from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        driver_id = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Driver.objects.filter(driver_id=driver_id).count() == 0:
            break

    return driver_id


# Create your models here.
class Driver(models.Model):
    driver_id = models.CharField(max_length=10, default=generate_unique_code, unique=True)
    driver_name = models.CharField(max_length=30, default="", unique=False)
    driver_email = models.CharField(max_length=50)
    taxi_num = models.CharField(max_length=10, unique=True)
    driver_phone = models.CharField(max_length=11)
    taxi_test_date = models.DateField(auto_now=False, auto_now_add=False,max_length=12) 
    taxi_pollution_validity = models.DateField(auto_now=False, auto_now_add=False,max_length=12)
    taxi_insurance = models.DateField(auto_now=False, auto_now_add=False,max_length=12)
    taxi_type = models.CharField(max_length=10,default='')
    taxi_model= models.CharField(max_length=10,default='')
    driver_status = models.CharField(max_length=10, default="available")
    driver_upi = models.CharField(max_length=10, default='', unique=True)


class ReceivedTrip(models.Model):
    user_name = models.CharField(max_length=250)
    start_from = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    requested_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
