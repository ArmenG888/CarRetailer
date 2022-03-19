from django.shortcuts import render
from .models import brand,car_model
def home(request):
    context = {
        'brands':brand.objects.all(),
    }
    return render(request,'cars/base.html', context)

def models(request,slug):
    context = {
        'brands':brand.objects.all(),
    }
    return render(request,'cars/base.html', context)