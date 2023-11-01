from django.urls import path
from apps.blog.views import index, details

urlpatterns = [
    path('blog/', index, name='blog'),
    path("blog/details/", details, name="details")
]
