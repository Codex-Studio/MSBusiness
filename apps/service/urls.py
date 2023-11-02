from django.urls import path
from apps.service.views import service, servise_details, servicestyle4

urlpatterns = [
    path('service/', service, name='service'),
    path('service_details/', servise_details, name='details'),
    path('service_style/', servicestyle4, name='service_style')
]
