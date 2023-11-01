from django.shortcuts import render
from apps.contact.models import Main, Contact, ContactAs
# Create your views here.
def contact(request):
    contact = Main.objects.latest('id')
    contact_all = Contact.objects.all()
    contact_as_id = ContactAs.objects.latest('id')
    return render(request, 'contact.html', locals())