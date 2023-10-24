from django.shortcuts import render
from apps.posts.models import Post
# Create your views here.
def index(request):
    index = Post.objects.all()
    return render(request, 'index.html', locals())
