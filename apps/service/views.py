from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.service.models import Service
from apps.service.forms import UserRegistarForm
# Create your views here.

def service(request):
    service_all = Service.objects.all()
    return render(request, 'service.html', locals())

#код для регистраций 
def register(request):

    if request.method == "POST":
        user_form = UserRegistarForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "my-account.html", {"user": new_user}, 'Пароль не совпадает, или такой аккаунт уже существует')
    else:
        user_form = UserRegistarForm()

    return render(request, "my-account.html", {"form": user_form}, 'Вы успешно прошли регистрацию')
