from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('services/', views.services),
    path('works/', views.works),
    path('contact/', views.contact),
    path('work-single/<int:no>/', views.workSingle),
    path('work-reg/', views.workReg),
    path('work-pro', views.workPro),
    path('work-modify/<int:no>/', views.workModify),
    path('work-remove/<int:no>/', views.workRemove),
]