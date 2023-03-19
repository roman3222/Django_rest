from django.contrib import admin

from .models import Sensor, TemperatureMeasurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(TemperatureMeasurement)
class TemperatureMeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor_description', 'temperature', 'created_at']

    def sensor_description(self, obj):
        return obj.sensor_id.description
    sensor_description.short_description = 'Sensor description'
