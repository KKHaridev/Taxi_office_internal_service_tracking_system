from rest_framework import serializers
from .models import Driver
from .models import ReceivedTrip


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< Updated upstream
            model = Driver
            fields = ('driver_id','driver_name','driver_email','taxi_num','driver_phone','driver_test_date','driver_pollution_validity','driver_insurance')

class CreateDriverSerializer(serializers.ModelSerializer):
      class Meta:
            model = Driver
            fields = ('driver_name','driver_email','taxi_num')
=======
        model = Driver
        fields = ('driver_id', 'driver_name', 'driver_email', 'taxi_num', 'driver_phone', 'driver_test_date',
                  'driver_pollution_validity', 'driver_insurance')


class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedTrip
        fields = ('user_name', 'start_from', 'destination', 'requested_time')
>>>>>>> Stashed changes
