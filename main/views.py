from django.contrib import messages
from django.shortcuts import render
from . import models
from .forms import Emailc
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
    if request.method == "POST":
        form = Emailc(request.POST)
        if form.is_valid():
            email=models.Email()
            email.Email = form.cleaned_data['Email']
            if models.Email.objects.get(Email=email.Email):
                messages.warning(request,"فرمت ایمیل درست نیست یا قبلا ثبت شده")
            else:
                email.save()
                messages.success(request,"شما عضو خبرنامه شدی")

    else:
        form = Emailc()

    return render(request,
    "index.html",
    {"data_banner":banner2,"ofpr":Offrs,
    "category":category,"allp":product_all,
    "banner":banner,"brand":brands,"form":form})
