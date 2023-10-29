from django.shortcuts import render
from apps.about.models import About, Companion, Develop, Achievement, Comand, Klient, Requests
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    comp = Companion.objects.latest('id')
    develop = Develop.objects.latest('id')
    achievemant_all = Achievement.objects.all()
    achievemant_id = Achievement.objects.latest('id')
    comand_all = Comand.objects.all()
    comand_id = Comand.objects.latest('id')
    klient_id = Klient.objects.latest('id')
    klient_all = Klient.objects.all()
    request_id = Requests.objects.latest('id')
    request_all = Requests.objects.all()
    return render(request, 'about-us.html', locals())