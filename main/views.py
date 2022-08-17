
from django.http import HttpResponseNotFound,HttpResponse
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
    "banner":banner,"brand":brands,"form":form,
    "ino":ino,"sabad":sabad,
    "saba":saba})



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
    co = models.comment.objects.all()
    commentCount = models.comment.objects.count()
    if pro:
        return render(request,"pro.html",{"pro":pro,"cate":cate,"prod":prod,"banner":banner,"comcount":commentCount,"comments":co})
    else:
        return HttpResponseNotFound("404") 
def next(request,id):
    try:
        if models.Product.objects.get(id=int(id)+1):
            return redirect(f"/pro/{int(id)+1}")
    except:
        for i in range(1,100):
            a = models.Product.objects.filter(id=i)
            if a:
                return redirect(f"/pro/{i}")
def sabt(request,id):
    if request.user.is_authenticated:
        pro = models.Product.objects.get(id=id)
        a = request.user.id
        models.sabad.objects.create(id_user=a,id_pro=pro.id)
        return HttpResponse("ok")
    else:
        messages.info(request,"شما عوض سایت نشدید")
        return redirect('/pro/')
def comment(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            a = request.POST['comment']
            aa = models.comment.objects.create(text = a,user_id=request.user.id,username=request.user,Product_id=id)
            
            messages.success(request,"کامنت شما ثبت شد")
            return redirect(f"../pro/{id}")
        else:
            messages.warning(request,"شما هنوز عضو سایت نشدید ")
            return redirect(f"../pro/{id}")

    else:
        return redirect(f"../pro/{id}")