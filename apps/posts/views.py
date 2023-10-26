from django.shortcuts import render
from django.http import HttpResponse
from apps.posts.models import Post, Job, Jobs, Main_About, Min_About, Direction, Direction_Main, Advantages, Advantage, ImageAdvantage, Status, Application, Applications, Applicati, Clients, Client, Footer, Foote
# Create your views here.
def index(request):
    try:
        index = Post.objects.all()
        job = Job.objects.all()
        jobs = Job.objects.latest("id")
        jobts = Jobs.objects.latest('id')
        about = Main_About.objects.all()
        about_min = Min_About.objects.all()
        dire = Direction.objects.all()
        directions = Direction_Main.objects.latest('id')
        advantages = Advantages.objects.latest('id')
        advantage = Advantages.objects.all()
        advan = Advantage.objects.latest('id')
        image = ImageAdvantage.objects.all()
        statu = Status.objects.all()
        app = Application.objects.latest('id')
        # applications = Applications.objects.latest('id')
        application = Applications.objects.all()
        appli = Applicati.objects.all()
        client = Clients.objects.latest('id')
        clients = Client.objects.all()
        foot = Footer.objects.latest('id')
        footer = Foote.objects.all()
    except Advantages.DoesNotExist:
        latest_advantage = None
    except Job.DoesNotExist:
        about_min = None
    except Min_About.ValueError:
        return HttpResponse("Не правильно указали данные")
    return render(request, 'index.html', locals())