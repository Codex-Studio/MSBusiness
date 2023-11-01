from django.contrib import admin
from apps.contact.models import Main, Contact, ContactAs
# Register your models here.
admin.site.register(Main)
admin.site.register(Contact)
admin.site.register(ContactAs)