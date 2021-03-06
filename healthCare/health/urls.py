from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('otp/', views.otp, name='otp'),
    path('about/', views.about, name='about'),
    path('signlog/', views.signlog, name='signlog'),

    path('emergency/', views.emergency, name='emergency'),
    path('emergencyhosp/', views.emergencyhosp, name='emergencyhosp'),
    
]