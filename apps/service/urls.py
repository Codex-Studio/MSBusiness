from django.urls import path
from apps.service.views import service, servise_details

urlpatterns = [
    path('service/', service, name='service'),
    path('service_details/', servise_details, name='details'),
    
]
