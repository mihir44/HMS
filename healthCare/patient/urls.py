from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='patient_home'),
    path('profile', views.profile, name='patient_profile'),
    path('appointment', views.appointment, name='appointment'),
    path('pappointment', views.patient_appointment_list, name='patient-view-appointment'),
    path('pappointment_delete/<int:pk>', views.patient_withdraw_appointment, name='patient_withdraw_appointment'),
    path('lab1', views.lab1, name='lab1'),
    path('lab2', views.lab2, name='lab2'),
    
]