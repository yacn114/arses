from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def main(request):
    Offrs = []
    banner2 = models.Image_trend_2.objects.all()
    banner = models.image_u.objects.first()
    product_all = models.Product.objects.all()
    brands = models.Brand.objects.all()
    for e in models.Product.objects.all():
        if e.price_offer != None:
            Offrs += models.Product.objects.filter(name= e)
    
    category = models.category.objects.all()
    return render(request,
    "index.html",
    {"data_banner":banner2,"ofpr":Offrs,
    "category":category,"allp":product_all,
    "banner":banner,"brand":brands})
