from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Patient(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    postal = models.IntegerField(default="")
    dob = models.DateField(default="")
    sex = (
        ("male", "Male"),
        ("female", "Female"),
        ("transgender", "Transgender"),
        ("not", "Rather not to say")
    )
    gender = models.CharField(max_length=50, choices=sex, default="male")

    @receiver(post_save, sender=User)
    def create_patient_profile(sender, instance,created,**kwargs):
        if created:
            Patient.object.create(user = instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()