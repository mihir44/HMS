from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('plogin/', views.patientLogin, name='patientlogin'),
    path('pregister/', views.patientRegister, name='patientregister'),
    path('hregister/', views.hospitalRegister, name='hospitalregister'),
    path('hlogin/', views.hospitalLogin, name='hospitallogin'),
    path('otp/', views.otp, name='otp'),
    path('about/', views.about, name='about'),
    path('signlog/', views.signlog, name='signlog'),

]