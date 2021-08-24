from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('login/', views.login),
    path('register/', views.register),
    path('otp/', views.otp),
]