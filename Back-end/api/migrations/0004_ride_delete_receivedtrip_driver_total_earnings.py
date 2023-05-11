# Generated by Django 4.2.1 on 2023-05-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_receivedtrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rideId', models.CharField(max_length=10, unique=True)),
                ('user_name', models.CharField(max_length=250)),
                ('start_from', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
                ('requested_time', models.DateTimeField(auto_now_add=True)),
                ('starting_time', models.DateTimeField()),
                ('reachedtime', models.DateTimeField()),
                ('expectedReachingtime', models.TimeField()),
                ('status', models.CharField(max_length=20)),
                ('carpool', models.BooleanField(default=False)),
                ('expectedDriverPay', models.CharField(max_length=7)),
                ('carpoolPercent', models.IntegerField(default=0, max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='ReceivedTrip',
        ),
        migrations.AddField(
            model_name='driver',
            name='total_earnings',
            field=models.IntegerField(default=0),
        ),
    ]