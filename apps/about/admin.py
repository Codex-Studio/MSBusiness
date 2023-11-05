from django.contrib import admin
from apps.about.models import About, Companion, Business, Team
# Register your models here.q
admin.site.register(About)
admin.site.register(Companion)
admin.site.register(Business)
admin.site.register(Team)