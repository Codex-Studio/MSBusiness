from django.contrib import admin
from apps.service.models import Service, Details, DetailsAll, ServiceDetails
# Register your models here.
admin.site.register(Service)
admin.site.register(Details)
admin.site.register(DetailsAll)
admin.site.register(ServiceDetails)