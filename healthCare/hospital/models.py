from uuid import uuid4

from django.db import models
from django.utils.deconstruct import deconstructible

from account.models import Patient, Hospital,User
import os

@deconstructible
class PathAndRename(object):
   def __init__(self, sub_path):
       self.path = sub_path

   def __call__(self, instance, filename):
       ext = "png"
       filename = '{}.{}'.format(uuid4().hex, ext)
       return os.path.join(self.path, filename)

class Doctor(models.Model):
    hospital = models.CharField(max_length=25, default="")
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    age = models.IntegerField()
    year_of_experience = models.IntegerField()
    degree = models.CharField(max_length=20, default="")
    sex = (
     ("male", "Male"),
     ("female", "Female"),
     ("transgender", "Transgender"),
     ("not", "Rather not to say")
    )
    gender = models.CharField(max_length=50, choices=sex, default="male")
    profile_pic = models.ImageField(upload_to=PathAndRename('uploads/doctors'),default="uploads/doctors/profile.png",null=True, blank=True)



