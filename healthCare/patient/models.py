from django.db import models
from account.models import Patient
# Create your models here
class Patient_profile(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal = models.IntegerField()
    dob = models.DateField()
    medical_history = models.CharField(max_length=25)
    gender = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.patient.username} Profile"


