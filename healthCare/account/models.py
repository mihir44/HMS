from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.html import escape,mark_safe

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

class Patient(models.Model):
    sex = (
        ("male", "Male"),
        ("female", "Female"),
        ("transgender", "Transgender")
    )
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE,)
    mobile = models.IntegerField()
    gender = models.CharField(choices=sex, default="male", max_length=15)
    address = models.CharField(max_length=250, default="")
    locations = (
        ('andheri', 'Andheri'),
        ('dadar', 'Dadar'),
        ('borivali', 'Borivali'),
        ('vile parle', 'Vile Parle'),
        ('goregaon', 'Goregaon'),
        ('churchgate', 'Churchgate'),
        ('mahim', 'Mahim'),
        ('grant road', 'Grant Road'),
        ('santacruz', 'Santacruz'),
        ('lower parel', 'Lower Parel'),
        ('sion', 'Sion'),
    )
    location = models.CharField(max_length=25, choices=locations, default="location")
    pincode = models.IntegerField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    history = models.CharField(max_length=250, default="")
    status = (
        ('single','Single'),
        ('married','Married'),
        ('widow','Widow')
    )
    marital_status = models.CharField(max_length=15,default='single')

class Hospital(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default="")
    locations = (
        ('andheri','Andheri'),
        ('dadar', 'Dadar'),
        ('borivali', 'Borivali'),
        ('vile parle', 'Vile Parle'),
        ('goregaon', 'Goregaon'),
        ('churchgate', 'Churchgate'),
        ('mahim', 'Mahim'),
        ('grant road', 'Grant Road'),
        ('santacruz', 'Santacruz'),
        ('lower parel', 'Lower Parel'),
        ('sion', 'Sion'),
    )
    location = models.CharField(max_length=25, choices=locations, default="location")
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