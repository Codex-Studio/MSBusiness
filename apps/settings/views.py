from django.shortcuts import render
from apps.settings.models import Settings, Service, OperationProcess, Benefits, Contact, Partner, Gellary,Project, ProjectoFeatures
# Create your views here.
def index(request):
    setting_all = Settings.objects.all()
    operetion_all = OperationProcess.objects.all()
    service_all = Service.objects.all()
    benefits_all = Benefits.objects.all()[:4]
    contact_all = Contact.objects.all()
    partner_all = Partner.objects.all()[:6]
    partner_id = Partner.objects.latest('id')
    return render(request, 'index.html', locals())

def contact(request):
    contact_id = Contact.objects.latest('id')
    return render(request, 'contact.html', locals())