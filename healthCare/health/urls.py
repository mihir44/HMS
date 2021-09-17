from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('otp/', views.otp, name='otp'),
    path('about/', views.about, name='about'),
    path('signlog/', views.signlog, name='signlog'),
     path('lab1/', views.lab1, name='lab1'),
    path('lab2/', views.lab2, name='lab2'),
    path('lab3/', views.lab3, name='lab3'),
]