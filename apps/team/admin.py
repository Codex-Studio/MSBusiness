from django.contrib import admin
from apps.team.models import Main, Team, TeamDetails, Team_Details, Experience, GetInTouch
# Register your models here.
admin.site.register(Main)
admin.site.register(Team)
admin.site.register(TeamDetails)
admin.site.register(Team_Details)
admin.site.register(Experience)
admin.site.register(GetInTouch)