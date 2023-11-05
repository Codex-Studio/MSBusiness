from django.shortcuts import render
from apps.about.models import About, Companion, Business, Team
from apps.settings.models import Partner
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    companio = Companion.objects.latest('id')
    business = Business.objects.latest('id')
    team_all = Team.objects.all()[:4]
    team_all2= Team.objects.all()[4:9]
    partners_all = Partner.objects.all()
    partners_id = Partner.objects.all()
    return render(request, 'about-us.html', locals())