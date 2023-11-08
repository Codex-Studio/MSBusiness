from django.shortcuts import render, redirect
from apps.settings.models import Settings, OperationProcess, Benefits, Contact, Partner, Project, ProjectoFeatures
from apps.service.models import Service
from django.core.mail import send_mail

# Create your views here.
def index(request):
    service_all = Service.objects.all().order_by('?')[:4]
    setting_all = Settings.objects.all()
    operetion_all = OperationProcess.objects.all()
    benefits_all = Benefits.objects.all()[:4]
    contact_all = Contact.objects.all()
    partner_all = Partner.objects.all()[:6]
    partner_id = Partner.objects.latest('id')
    return render(request, 'base/index.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    if request.method =="POST":
        name_surname = request.POST.get('name_surname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        Contact.objects.create(name_surname=name_surname, email=email, message=message, phone=phone)

        send_mail(
            f'{message}',

            f"""Здравствуйте {name_surname}.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваще сообщение: {message} 
            Ваша почта: {email}
            Ваш номер телефона {phone}
            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с правильными данными """,
            "noreply@somehost.local",
            [email])
        
        return redirect('index')

    return render(request, 'base/contact.html', locals())