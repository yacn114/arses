from django.urls import path
from . import views
app_name = "details"
urlpatterns = [
    path('factors',views.factor,name="factor"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
]
