from django import template
from django.http import HttpResponseRedirect
from main import models
register = template.Library()
@register.simple_tag
def takhfif(price, price_offer, *args, **kwargs):
    resualt = int((price/100)*int(str(price_offer)[0:2])-price)*-1
    return resualt


