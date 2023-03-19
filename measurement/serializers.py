from rest_framework import serializers

from measurement.models import Sensor, TemperatureMeasurement



class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['temperature', 'created_at']
        read_only_fields = ['id']


class SensorSerializer(serializers.ModelSerializer):
    measurement = TemperatureMeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']
