from django.shortcuts import render, redirect
from apps.settings.models import Settings
from .models import Team, Contact_Team


# Create your views here.
def team(request):
    settings = Settings.objects.latest("id")
    team = Team.objects.all()
    return render(request, "team/team.html",locals())

def team_single(request, id):
    team = Team.objects.get(id=id)
    settings = Settings.objects.latest('id')

    return render (request, "team/team-detail.html", locals())