from django.urls import path
from . import views
app_name = "details"
urlpatterns = [
    path('factors',views.factor,name="factor"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('my-account',views.account,name="account"),
    path('security',views.security,name="security"),
    path('c/<parametr>',views.category,name="security"),
]
