from . import views
from django.urls import path

urlpatterns = [
    path('',views.main),
    path('search',views.search),
    path('likes/<id>',views.likes),
    path('pro/<id>',views.pro),
    path('sabad/<id>',views.sabad),
    path('next/<id>',views.next),
    path('sabt/<id>',views.sabt),
    path('com/<id>',views.comment),

    
]
