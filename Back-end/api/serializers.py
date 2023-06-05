from rest_framework import serializers
# from .models import Driver, Ride
from .models import TaxiDetail, NewDriver, NewRideDetail, Earning





# class TaxiDetails(serializers.Serializer):
#     taxi_num = serializers.CharField(max_length=15), 
#     taxi_test_date = serializers.DateField(),
#     taxi_pollution_validity = serializers.DateField(),
#     taxi_insurance = serializers.DateField(),
#     taxi_type = serializers.CharField(max_length=15),
#     taxi_model = serializers.CharField(max_length=15),

# class DriverWithTaxiDetails(serializers.ModelSerializer):
#     taxi_det = TaxiDetails(many=True)

#     class Meta:
#         model = NewDriver
#         fields = ('driver_id', 'driver_name', 'driver_email', 'driver_phone',  'driver_status', 'driver_upi','taxi_det')
#         depth = 1





# class NewDriverSerializer(serializers.ModelSerializer):
#     driver_id = serializers.CharField(max_length=10, default=generate_unique_code)
#     driver_name = serializers.CharField(max_length=30, default="")
#     driver_email = serializers.CharField(max_length=50)
#     driver_phone = serializers.CharField(max_length=11)
#     driver_upi = serializers.CharField(max_length=15, default='')
#     taxi_num = serializers.PrimaryKeyRelatedField(queryset=TaxiDetails.objects.all())
#     taxi_test_date = serializers.DateField()
#     taxi_pollution_validity = serializers.DateField()
#     taxi_insurance = serializers.DateField()
#     taxi_type = serializers.CharField(max_length=10, default='')
#     taxi_model = serializers.CharField(max_length=10, default='')

#     class Meta:
#         model = NewDriver
#         fields = ('driver_id', 'driver_name', 'driver_email', 'driver_phone', 'driver_upi', 'taxi_num',
#                   'taxi_test_date', 'taxi_pollution_validity', 'taxi_insurance', 'taxi_type', 'taxi_model')





class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDriver
        fields = ('driver_id', 'driver_name', 'driver_email', 'driver_phone',  'driver_status', 'driver_upi',)




class CreateDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDriver
        fields = ('driver_name', 'driver_email', 'driver_phone', 'driver_status', 'driver_upi')

class CreateTaxiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiDetail
        fields = '__all__'

class CreateNewRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRideDetail
        fields = ('passenger_name','driver_name', 'start_from', 'destination', 'requested_time','status')

class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRideDetail
        fields = ('passenger_name', 'start_from', 'destination',
                  'requested_time', 'status')


class CompletedRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRideDetail
        fields = ('rideId', 'passenger_name', 'start_from',
                  'destination', 'reachedtime', 'status')


class EarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = ('total_rides', 'total_earnings',
                  'total_paid', 'total_pending')


class OngoingRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRideDetail
        fields = ('rideId','passenger_name', 'start_from', 'destination', 'starting_time',
                  'expectedDriverPay', 'status', 'carpoolPercent')

class CancelledRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRideDetail
        fields = ('rideId', 'passenger_name', 'start_from',
                  'destination', 'status')
    
class DriverDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = ('driver_id','total_earnings','total_rides')