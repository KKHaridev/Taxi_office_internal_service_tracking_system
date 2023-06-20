# Generated by Django 4.2 on 2023-06-01 16:21

from api.models import unique_generator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_ride_carpoolpercent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_earnings', models.IntegerField(default=0)),
                ('total_rides', models.IntegerField(default=0)),
                ('total_paid', models.IntegerField(default=0)),
                ('total_pending', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NewDriver',
            fields=[
                ('driver_id', models.CharField(default=unique_generator.generate_unique_code_for_driverid, max_length=10, primary_key=True, serialize=False)),
                ('driver_name', models.CharField(default='', max_length=30)),
                ('driver_email', models.CharField(max_length=50)),
                ('driver_upi', models.CharField(default='', max_length=15, unique=True)),
                ('driver_phone', models.CharField(max_length=11)),
                ('driver_dob', models.DateTimeField()),
                ('driver_status', models.CharField(default='available', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NewRideDetails',
            fields=[
                ('rideId', models.CharField(default=unique_generator.generate_unique_code_for_rideid, max_length=10, primary_key=True, serialize=False)),
                ('passenger_name', models.CharField(max_length=250)),
                ('start_from', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
                ('requested_time', models.DateTimeField(auto_now_add=True)),
                ('starting_time', models.DateTimeField()),
                ('reachedtime', models.DateTimeField()),
                ('expectedReachingtime', models.TimeField()),
                ('status', models.CharField(max_length=20)),
                ('carpool', models.BooleanField(default=False)),
                ('expectedDriverPay', models.CharField(max_length=7)),
                ('carpoolPercent', models.IntegerField(default=0)),
                ('driver_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='api.newdriver')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiDetails',
            fields=[
                ('taxi_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('taxi_test_date', models.DateField(max_length=12)),
                ('taxi_pollution_validity', models.DateField(max_length=12)),
                ('taxi_insurance', models.DateField(max_length=12)),
                ('taxi_type', models.CharField(default='', max_length=10)),
                ('taxi_manufacturer', models.CharField(default='', max_length=10)),
                ('taxi_model', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Ride',
        ),
        migrations.AddField(
            model_name='newdriver',
            name='taxi_num',
            field=models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.DO_NOTHING, to='api.taxidetails'),
        ),
        migrations.AddField(
            model_name='earnings',
            name='driver_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='api.newdriver'),
        ),
    ]
