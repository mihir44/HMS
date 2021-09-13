from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.html import escape,mark_safe

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField(max_length=10)

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField(max_length=10)