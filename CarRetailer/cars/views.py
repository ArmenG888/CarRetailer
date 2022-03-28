from django.shortcuts import render
from .models import brand,car_model
from django.views.generic import DetailView

def home(request):
    for x in brand.objects.all():
        cars_related = x.car_model_set.all()
        x.cars_to_brand.set(cars_related)
        x.save()
    context = {
        'cars':brand.objects.all(),
    }
    return render(request,'cars/base.html', context)
def brands(request):
    context = {
        'brands':brand.objects.all(),
    }
    return render(request,'cars/brands.html', context)

class BrandDetailView(DetailView):
    model = brand