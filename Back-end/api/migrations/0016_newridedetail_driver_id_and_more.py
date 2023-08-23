# Generated by Django 4.2 on 2023-06-21 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_newridedetail_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newridedetail',
            name='driver_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.newdriver'),
        ),
        migrations.AlterField(
            model_name='newridedetail',
            name='driver_name',
            field=models.CharField(max_length=100),
        ),
    ]
