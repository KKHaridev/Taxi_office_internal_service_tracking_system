from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_id = models.CharField(max_length=10,default="",unique=True)
    driver_name = models.CharField(max_length=30,default="",unique=False)
    driver_email =models.CharField(max_length=50)
    taxi_num = models.CharField(max_length=10,unique=True)
    driver_phone = models.CharField(max_length=11)
    driver_test_date = models.DateField(auto_now=False, auto_now_add=False,max_length=12) 
    driver_pollution_validity = models.DateField(auto_now=False, auto_now_add=False,max_length=12)
    driver_insurance = models.DateField(auto_now=False, auto_now_add=False,max_length=12)
    
    