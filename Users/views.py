# from .models import User
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def auth(request):
    if request.method == "POST":
        name = str(request.POST['name'])
        phone = int(request.POST['phone'])
    else:
        return HttpResponseRedirect("../signup")
def signup(request):
    return render(request,'user.html',{"mmd":AuthenticationForm})
    