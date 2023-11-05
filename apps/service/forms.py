from django import forms
from apps.service.models import Service

class UserRegistarForm(forms.ModelForm):
    email = forms.CharField(label='Адрес Элестронной почты', widget=forms.EmailInput)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput)

    class Meta:
        model = Service 
        fields = '__all__'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd["password2"]