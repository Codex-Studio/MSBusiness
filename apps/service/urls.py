from django.urls import path
from apps.service.views import service, servise_details, service_style4, service_style6

urlpatterns = [
    path('service/', service, name='service'),
    path('service_details/', servise_details, name='details'),
    path('service_style4/', service_style4, name='service_style4'),
    path('service_style6/', service_style6, name='service_style6')

]
