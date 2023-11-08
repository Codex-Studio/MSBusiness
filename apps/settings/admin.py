from django.contrib import admin
from apps.settings.models import Settings, OperationProcess, Benefits, Contact, Partner, Project, ProjectoFeatures
# Register your models here.
admin.site.register(Settings)
admin.site.register(OperationProcess)
admin.site.register(Benefits)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Project)
admin.site.register(ProjectoFeatures)