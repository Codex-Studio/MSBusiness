from django.urls import path
from apps.blog.views import index

urlpatterns = [
    path('blog/', index, name='blog')
]
