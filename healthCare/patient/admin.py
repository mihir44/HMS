from django.contrib import admin
from .models import Patient_profile, Appointment,Product, Category, Order
# Register your models here.
admin.site.register(Patient_profile),
admin.site.register(Appointment),
admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Order),
