from django import template
from django.http import HttpResponseRedirect
from main import models
register = template.Library()
@register.simple_tag
def takhfif(price, price_offer, *args, **kwargs):
    resualt = int((price/100)*int(str(price_offer)[0:2])+(price*-1))
    return resualt
@register.simple_tag
def next(id, *args, **kwargs):
    obj = models.Product.get(id=id+1)
    if obj:
        return HttpResponseRedirect(f"/pro/{id+1}")