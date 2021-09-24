from django.db import models
<<<<<<< HEAD
from account.models import Patient, Hospital
# Create your models here
class Patient_profile(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal = models.IntegerField()
    dob = models.DateField()
    medical_history = models.CharField(max_length=25)
    sex = (
        ("male", "Male"),
        ("female", "Female"),
        ("transgender", "Transgender"),
        ("not", "Rather not to say")
    )
    gender = models.CharField(max_length=50, choices=sex, default="male")

    def __str__(self):
        return f"{self.patient.patient.user.username} Profile"

class Appointment(models.Model):
        """Contains info about appointment"""
        TIMESLOT_LIST = (
            (0, '09:00 – 10:00'),
            (1, '10:00 – 11:00'),
            (2, '11:00 – 12:00'),
            (3, '12:00 – 13:00'),
            (4, '13:00 – 14:00'),
            (5, '14:00 – 15:00'),
            (6, '15:00 – 16:00'),
            (7, '16:00 – 17:00'),
            (8, '17:00 – 18:00'),
        )
        hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
        date = models.DateField()
        timeslot = models.IntegerField(choices=TIMESLOT_LIST)
        patient_name = models.CharField(max_length=60)
=======

>>>>>>> 47bc73da4dd6665836b0b17418d066c55bd9b616


