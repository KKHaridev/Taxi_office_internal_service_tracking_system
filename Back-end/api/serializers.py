from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
            model = Driver
            fields = ('driver_id','driver_name','driver_email','taxi_num','driver_phone','driver_test_date','driver_pollution_validity','driver_insurance')
        