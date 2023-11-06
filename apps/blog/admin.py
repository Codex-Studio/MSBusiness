from django.contrib import admin
from apps.blog.models import Blog, OurProjects, BlogDetails, Details
# Register your models here.
admin.site.register(Blog)
admin.site.register(OurProjects)
admin.site.register(BlogDetails)
admin.site.register(Details)