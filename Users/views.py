from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def auth(request):
    return HttpResponse("ok")
def signup(request):
    return render(request,'user.html',{"mmd":AuthenticationForm})
