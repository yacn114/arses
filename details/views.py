from django.http import HttpResponse
from django.shortcuts import render

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
def category(request,parametr):
    return HttpResponse(f"ok {parametr}")