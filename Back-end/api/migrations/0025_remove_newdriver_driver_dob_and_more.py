# Generated by Django 4.2 on 2023-06-23 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_newridedetail_driver_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newdriver',
            name='driver_dob',
        ),
        migrations.RemoveField(
            model_name='newridedetail',
            name='driver_name',
        ),
    ]
