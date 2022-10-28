from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('services/', views.services),
    path('works/', views.works),
    path('contact/', views.contact),
    path('work-reg/', views.workReg),
    path('work-pro', views.workPro),
]