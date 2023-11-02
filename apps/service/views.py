from django.shortcuts import render
from apps.service.models import Main, Services, ServiceTitle, ServiceDetails, Team, TeamWide, Consulting, Business, Style, Success, Style6, Insurance
# Create your views here.
def service(request):
    # setti
    main = Main.objects.latest('id')
    service_id = ServiceTitle.objects.latest("id")
    service_all = Services.objects.all()
    return render(request, 'service.html', locals())

def servise_details(request):
    service_details = ServiceDetails.objects.latest('id')
    team_id = Team.objects.latest('id')
    team_all = Team.objects.all()
    wide_id = TeamWide.objects.latest('id')
    wide_all = TeamWide.objects.all()
    consulting_all = Consulting.objects.all()
    consulting_id = Consulting.objects.latest('id')
    busines_id = Business.objects.latest('id')
    busines_all = Business.objects.all()
    return render(request, 'service-details.html', locals())


def service_style4(request):
    style = Style.objects.latest('id')
    success_id = Success.objects.latest('id')
    success_all = Success.objects.all()
    return render(request, 'service-style-4.html', locals())


def service_style6(request):
    style = Style6.objects.latest('id')
    insurance_id = Insurance.objects.latest('id')
    insurance_all = Insurance.objects.all()
    return render(request, 'service-style-6.html', locals())