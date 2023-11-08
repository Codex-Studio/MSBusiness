from django.shortcuts import render
from apps.settings.models import Settings
from .models import Service

# Create your views here.
def service(request):
    settings = Settings.objects.latest('id')
    service_all = Service.objects.all()
    return render(request, 'service/service.html', locals())

def services_detail(request,id):
    settings = Settings.objects.latest('id')
    service = Service.objects.get(id=id) 
    return render(request, "service/service-details.html",locals())