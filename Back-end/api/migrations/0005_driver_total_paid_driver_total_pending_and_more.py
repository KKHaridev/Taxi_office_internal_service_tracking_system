# Generated by Django 4.2 on 2023-05-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_ride_delete_receivedtrip_driver_total_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='total_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='driver',
            name='total_pending',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='driver',
            name='total_rides',
            field=models.IntegerField(default=0),
        ),
    ]
