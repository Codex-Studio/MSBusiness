from django.urls import path
from apps.pricind.views import pricing

urlpatterns = [
    path('pricing/', pricing, name='pricing')
]
