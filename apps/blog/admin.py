from django.contrib import admin
from apps.blog.models import Main, Projects, BlogDetails, Business
# Register your models here.
admin.site.register(Main)
admin.site.register(Projects)
admin.site.register(BlogDetails)
admin.site.register(Business)

