from django.shortcuts import render
from apps.about.models import Review, About, Team
from apps.settings.models import Partner
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    review_all = Review.objects.all()
    team_all = Team.objects.all()
    partner_all = Partner.objects.all()
    partner_id = Partner.objects.latest('id')
    return render(request, 'about-us.html', locals())