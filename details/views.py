
from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from . import models
from main.models import Image_trend_2,Product,category,sabad,interest

# Create your views here.
def factor(request):
    pass
def about(request):
    pass
def contact(request):
    pass
def account(request):
    pass
def security(request):
    pass
def categoryview(request,parametr):
    return HttpResponse(f"ok {parametr}")
def pro(request,id):
    banner = Image_trend_2.objects.all()
    pro = Product.objects.get(id=id)
    prod = Product.objects.all()
    saba = sabad.objects.all()
    cate = category.objects.all()
    sabad1 = sabad.objects.count()
    ino = interest.objects.count()
    co = models.comment.objects.all()
    buyful = Product.objects.all().order_by('buyers')[:10]
    commentCount = models.comment.objects.filter(id=id).count()
    if pro:
        return render(request,"pro.html",{"pro":pro,"cate":cate,"allp":prod,"banner":banner,"comcount":commentCount,"comments":co,"sabad":sabad1,"ino":ino,"saba":saba,
        "buy":buyful})
    else:
        return HttpResponseNotFound("404") 
def next(request,id):
    try:
        if Product.objects.get(id=int(id)+1):
            return redirect(f"/pro/{int(id)+1}")
    except:
        for i in range(1,100):
            a = Product.objects.filter(id=i)
            if a:
                return redirect(f"/pro/{i}")

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