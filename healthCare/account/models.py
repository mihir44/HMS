from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.html import escape,mark_safe

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

class Patient(models.Model):
    phone_number = models.IntegerField()
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE,)

class Hospital(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default="")
    locations = (
        ('andheri','Andheri'),
        ('dadar', 'Dadar'),
        ('borivali', 'Borivali'),
        ('vile parle', 'Vile Parle'),
        ('goregaon', 'Goregaon'),
        ('goregaon', 'Goregaon'),
        ('churchgate', 'Churchgate'),
        ('mahim', 'Mahim'),
        ('grant road', 'Grant Road'),
        ('santacruz', 'Santacruz'),
        ('lower parel', 'Lower Parel'),
        ('sion', 'Sion'),
    )
    location = models.CharField(max_length=20, choices=locations, default="location")
    mobile = models.IntegerField()
    pincode = models.IntegerField()
    wards = models.IntegerField()
    doctors = models.IntegerField()
    tariff = models.IntegerField()
    medical = models.IntegerField()
    service = (
        ('yes', 'Yes'),
        ('no', 'No')
    )
    emergency = models.CharField(max_length=3, choices=service, default="No")
    beds = models.IntegerField()
    incharge = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.doctor.username