from django.urls import path
from apps.business.views import business, range

urlpatterns = [
    path('service-strle4/', business, name='style'),
    path('service-style6/', range, name='range'),
]
