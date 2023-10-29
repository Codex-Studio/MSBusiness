from django.shortcuts import render
from apps.blog.models import Main, Projects
# Create your views here.
def index(request):
    main_id = Main.objects.latest('id')
    project_all = Projects.objects.all()
    return render(request, 'blog.html', locals())
