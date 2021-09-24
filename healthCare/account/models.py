from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.html import escape,mark_safe

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, )
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=30,default="")
    state = models.CharField(max_length=30,default="")
    postal = models.IntegerField(default="")
    dob = models.DateField(default="")
    sex = (
        ("male", "Male"),
        ("female","Female"),
        ("transgender","Transgender"),
        ("not","Rather not to say")
    )
    gender = models.CharField(max_length=50, choices=sex, default="male")


class Hospital(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.doctor.username