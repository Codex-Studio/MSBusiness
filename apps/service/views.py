from django.shortcuts import render
from apps.service.models import Main, Services, ServiceTitle, ServiceDetails, Team, TeamWide, Consulting, Business
# Create your views here.
def service(request):
    # setti
    main = Main.objects.latest('id')
    service_id = ServiceTitle.objects.latest("id")
    service_all = Services.objects.all()
    return render(request, 'service.html', locals())

def servise_details(request):
    service_details = ServiceDetails.objects.latest('id')
    team = Team.objects.latest('id')
    wide_id = TeamWide.objects.latest('id')
    wide_all = TeamWide.objects.all()
    consulting_all = Consulting.objects.all()
    consulting_id = Consulting.objects.latest('id')
    busines_id = Business.objects.latest('id')
    busines_all = Business.objects.all()
    return render(request, 'service-details.html', locals())