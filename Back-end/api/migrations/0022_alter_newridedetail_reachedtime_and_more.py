# Generated by Django 4.2 on 2023-06-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_newridedetail_driver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newridedetail',
            name='reachedtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='newridedetail',
            name='starting_time',
            field=models.DateTimeField(null=True),
        ),
    ]