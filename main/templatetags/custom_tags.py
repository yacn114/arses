
from django import template

from ..models import jamsabad
register = template.Library()
@register.simple_tag
def takhfif(price, price_offer, *args, **kwargs):
    resualt = int((price/100)*int(str(price_offer)[0:2])-price)*-1
    return f"{resualt:,}"

@register.simple_tag
def jam(price,price_offer, t, *args, **kwargs):
    a = ""
    for i in takhfif(price,price_offer).split(","):
        a += i
    
    resualt = int(a) * t
    return f"{resualt:,}"
@register.simple_tag
def format(resualt,*args, **kwargs):
    return f"{resualt:,}"
@register.simple_tag
def jam2(price,price_offer, T, *args, **kwargs):
    array = 0
    count=""
    for a in jam(price,price_offer,T):
        for i in a.split(","):
            count += i
        array += int(count)

    return f"{array:,}"