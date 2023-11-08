from django.urls import path

from .views import service, services_detail

urlpatterns = [
    path('service/', service, name="service"),
    path('services_detail/<int:id>/', services_detail, name="services_detail"),
]