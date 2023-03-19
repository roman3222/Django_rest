from django.urls import path

from measurement.views import create_sensor, get_all_sensor, SensorView, add_measurement, UpdateSensorView

urlpatterns = [
    path('create/', create_sensor),
    path('all_sensor/', get_all_sensor),
    path('sensor/<pk>/', SensorView.as_view()),
    path('add_measure/', add_measurement),
    path('update/<int:pk>/', UpdateSensorView.as_view(), name='update'),
]
