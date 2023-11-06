from django.shortcuts import render
from apps.blog.models import Blog, OurProjects, BlogDetails, Details
# Create your views here.
def blog(request):
    blog = Blog.objects.latest('id')
    project_all = OurProjects.objects.all()
    return render(request, 'blog.html', locals())

def details(request):
    blog = BlogDetails.objects.latest('id')
    deatils_all = Details.objects.all()
    return render(request, 'blog-details.html', locals())