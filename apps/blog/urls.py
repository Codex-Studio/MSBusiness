from django.urls import path
from apps.blog.views import blog, details

urlpatterns = [
    path('blog/', blog, name='blog'), 
    path('blog-details/', details, name='blog-details'),
]