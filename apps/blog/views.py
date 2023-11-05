from django.shortcuts import render
from apps.blog.models import Blog, OurProjects
# Create your views here.
def blog(request):
    blog = Blog.objects.latest('id')
    project_all = OurProjects.objects.all()
    return render(request, 'blog.html', locals())