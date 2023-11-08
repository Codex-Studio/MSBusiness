
from django.shortcuts import render
from apps.blog.models import Blog
# Create your views here.
def blog(request):
    blog_all = Blog.objects.all()
    return render(request, 'blog/blog.html', locals())

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/blog-details.html', locals())
