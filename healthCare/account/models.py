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
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,)
    phone_number = models.IntegerField()