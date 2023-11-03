from django.urls import path
from apps.team.views import team, details

urlpatterns = [
    path('team/', team, name='team'),
    path('team-detail', details, name='details')
]