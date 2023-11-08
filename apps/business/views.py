from django.shortcuts import render
from apps.business.models import Benefist, Range
# Create your views here.
def business(request):
    business_all = Benefist.objects.all()
    return render(request, 'service/service-style-4.html', locals())


def range(request):
    range_all = Range.objects.all()
    return render(request, 'service/service-style-6.html', locals())