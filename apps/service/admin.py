from django.contrib import admin
from apps.service.models import Main, Services,ServiceTitle, ServiceDetails, Team, TeamWide, Consulting, Business
# Register your models here.
admin.site.register(Main)
admin.site.register(Services)
admin.site.register(ServiceTitle)
admin.site.register(ServiceDetails)
admin.site.register(Team)
admin.site.register(TeamWide)
admin.site.register(Consulting)
admin.site.register(Business)