from django.urls import path

from apps.blog.views import blog, blog_details

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog-details/<int:id>/', blog_details, name="blog-details"),
]
