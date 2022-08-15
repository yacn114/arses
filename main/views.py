from django.http import HttpResponseNotFound
from django.contrib import messages
from django.shortcuts import render,redirect
from . import models
from .forms import Emailc
# Create your views here.

def main(request):
    Offrs = []
    banner2 = models.Image_trend_2.objects.all()
    banner = models.image_u.objects.first()
    product_all = models.Product.objects.all()
    sabad = models.sabad.objects.count()
    saba = models.sabad.objects.all()
    ino = models.interest.objects.count()
    brands = models.Brand.objects.all()
    ofpm = {}
    for e in models.Product.objects.all():
        if e.price_offer != None:
            ofpm.update({"gh" : int((e.price/100)*int(str(e.price_offer)[0:2])+(e.price*-1)),"user_id":e.id})
            
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
    "banner":banner,"brand":brands,"form":form,
    "ino":ino,"sabad":sabad,
    "saba":saba,"ghymt":ofpm.keys()})



def search(request):
    if request.method == "POST":
        print("ok")

def sabadolikes(request):
    models.sabad.objects.all()
    models.interest.objects.all()
    pass
def likes(request,id):
    try:
        pro = models.Product.objects.get(id=id)
        a = request.user.id
        models.interest.objects.create(user_id=a,pro_id=pro)
        return "ok"
    except:
        messages.info(request,"شما عوض سایت نشدید")
        return redirect('/')
def sabad(request,id):
    try:
        pro = models.Product.objects.get(id=id)
        a = request.user.id
        models.sabad.objects.create(user_id=a,pro_id=pro)
        return "ok"
    except:
        messages.info(request,"شما عوض سایت نشدید")
        return redirect('/')
def pro(request,id):
    banner = models.Image_trend_2.objects.all()
    pro = models.Product.objects.get(id=id)
    prod = models.Product.objects.all()
    cate = models.category.objects.all()
    if pro:
        return render(request,"pro.html",{"pro":pro,"cate":cate,"prod":prod,"banner":banner})
    else:
        return HttpResponseNotFound("404") 
