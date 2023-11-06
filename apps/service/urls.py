from django.urls import path
from apps.service.views import service, register, details

urlpatterns = [
    path('service/', service, name='service'),
    path('my-account/', register, name='register'),
    path('details', details, name='service-details'),
]
