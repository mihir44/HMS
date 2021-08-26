from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('plogin/', views.patientLogin),
    path('pregister/', views.patientRegister),
    path('otp/', views.otp),
    path('index/', views.index),
]