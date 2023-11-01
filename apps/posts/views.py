from django.shortcuts import render
from apps.posts.models import Main, Job, About, Directions, Advantages, Description, Application, Klient

def index(request):
    index = Main.objects.all()
    job_id = Job.objects.latest('id')
    job_all = Job.objects.all()
    about_id = About.objects.latest('id')
    directions_id = Directions.objects.latest('id')
    directions_all = Directions.objects.all()
    advantages_id = Advantages.objects.latest('id')
    advantages_all = Advantages.objects.all().order_by('?')[:2]
    descriptions_all = Description.objects.all()
    descriptions_id = Description.objects.latest('id')
    application_id = Application.objects.latest('id')
    application_all = Application.objects.all()
    klient_id = Klient.objects.latest('id')
    klient_all = Klient.objects.all()
    return render(request, 'index.html', locals())
