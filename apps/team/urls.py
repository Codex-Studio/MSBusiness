from django.urls import path
from apps.team.views import team

urlpatterns = [
    path('team/', team, name='team')
]