# Generated by Django 4.1.7 on 2023-03-18 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_date_measurement_temperaturemeasurement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
