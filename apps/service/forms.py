from django import forms
from apps.service.models import Services

class ServicesMainForm(forms.Form):
    class Meta:
        model = Services
        fields = ['title', 'context']

class ServicesForm(forms.Form):
    class Meta:
        model = Services
        fields = ['image', 'image_title', 'image_context', 'end_image']
