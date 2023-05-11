from rest_framework import serializers
from .models import Driver, Ride


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_id', 'driver_name', 'driver_email', 'taxi_num', 'driver_phone', 'taxi_test_date',
                  'taxi_pollution_validity', 'taxi_insurance', 'taxi_type', 'taxi_model', 'driver_status', 'driver_upi')


class CreateDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_name', 'driver_email', 'taxi_num')


class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('user_name', 'start_from', 'destination',
                  'requested_time', 'status')


class CompletedRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('RideId', 'user_name', 'start_from',
                  'destination', 'reachedtime', 'status')


class EarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('total_rides', 'total_earnings',
                  'total_paid', 'total_pending')


class OngoingRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('RideId', 'user_name', 'start_from', 'destination', 'starting_time',
                  'expectedDriverPay', 'status', 'carpoolPercent')
