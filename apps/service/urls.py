from django.urls import path
from apps.service.views import service, register

urlpatterns = [
    path('service/', service, name='service'),
    path('my-account/', register, name='register'),
]
