from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='patient_home'),
    path('profile', views.profile, name='patient_profile'),
    path('appointment',views.appointment, name='appointment'),
]