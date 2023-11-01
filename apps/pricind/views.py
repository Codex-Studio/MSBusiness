from django.shortcuts import render
from apps.pricind.models import Main, Escort, Questions, Questions2
# Create your views here.
def pricing(request):
    pricing = Main.objects.latest('id')
    escort_id = Escort.objects.latest('id')
    escort_all = Escort.objects.all()
    question_id = Questions.objects.latest('id')
    question_all = Questions.objects.all()
    question2_all = Questions2.objects.all()
    return render(request, 'pricing.html', locals())