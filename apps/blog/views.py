from django.shortcuts import render
from apps.blog.models import Main, Projects, BlogDetails, Business
# Create your views here.
def index(request):
    main_id = Main.objects.latest('id')
    project_all = Projects.objects.all()
    return render(request, 'blog.html', locals())

def details(request):
    blog = BlogDetails.objects.latest('id')
    business_id = Business.objects.latest('id')
    business_all = Business.objects.all()
    return render(request, 'blog-details.html', locals())