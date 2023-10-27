from django.urls import path
from apps.service.views import service

urlpatterns = [
    path('service/', service, name='service')
    
]
