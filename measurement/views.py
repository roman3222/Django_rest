from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer


@api_view(['POST'])
def create_sensor(request):
    serializer = SensorSerializer(data=request.query_params)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSensorView(APIView):
    def put(self, request, pk, format=None):
        name = request.query_params.get('name')
        description = request.query_params.get('description')
        try:
            sensor = Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SensorSerializer(sensor, data={'name': name, 'description': description})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_measurement(request):
    temperature = request.query_params.get('temperature')
    sensor_id = request.query_params.get('id')
    if not sensor_id:
        sensor_id = 1

    serializer = TemperatureMeasurementSerializer(data={'temperature': temperature, 'sensor_id': sensor_id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_sensor(request):
    sensor = Sensor.objects.all()
    ser = SensorSerializer(sensor, many=True)
    return Response(ser.data, status=status.HTTP_201_CREATED)


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer















