# Generated by Django 4.2 on 2023-06-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_newridedetail_reachedtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newridedetail',
            name='expectedDriverPay',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='newridedetail',
            name='expectedReachingtime',
            field=models.TimeField(null=True),
        ),
    ]