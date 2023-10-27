from django.shortcuts import render
from apps.service.models import Main, Services, ServiceTitle
from apps.posts.models import Post
# Create your views here.
def service(request):
    # setti
    main = Main.objects.latest('id')
    service_id = ServiceTitle.objects.latest("id")
    service_all = Services.objects.all()
    return render(request, 'service.html', locals())