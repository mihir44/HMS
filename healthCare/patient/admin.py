from django.contrib import admin
from .models import Patient_profile, Appointment
# Register your models here.
admin.site.register(Patient_profile),
admin.site.register(Appointment),