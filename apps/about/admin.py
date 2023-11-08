from django.contrib import admin
from apps.about.models import Team, Review, About
# Register your models here.
admin.site.register(Team)
admin.site.register(Review)
admin.site.register(About)