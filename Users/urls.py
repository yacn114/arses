from django.urls import path
from . import views
urlpatterns = [
    path('login',views.auth,name="auth"),
    path('signup',views.signup),
    
]
