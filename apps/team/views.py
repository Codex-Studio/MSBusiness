from django.shortcuts import render
from apps.team.models import Main, Team
# Create your views here.
def team(request):
    main = Main.objects.latest('id')
    team_id = Team.objects.latest('id')
    team_all = Team.objects.all()
    return render(request, 'team.html', locals())