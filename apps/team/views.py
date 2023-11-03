from django.shortcuts import render
from apps.team.models import Main, Team, TeamDetails, Team_Details, Experience, GetInTouch
# Create your views here.
def team(request):
    main = Main.objects.latest('id')
    team_id = Team.objects.latest('id')
    team_all = Team.objects.all()
    return render(request, 'team.html', locals())

def details(request):
    team = TeamDetails.objects.latest('id')
    team_details = Team_Details.objects.latest('id')
    experience_id = Experience.objects.latest('id')
    experience_all = Experience.objects.all()
    getintouch = GetInTouch.objects.latest('id')
    return render(request, 'team-detail.html', locals())