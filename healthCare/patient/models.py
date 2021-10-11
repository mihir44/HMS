from django.db import models
from account.models import Patient, Hospital,User
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
            ('09:00 – 10:00', '09:00 – 10:00'),
            ('10:00 – 11:00', '10:00 – 11:00'),
            ('11:00 – 12:00', '11:00 – 12:00'),
            ('12:00 – 13:00', '12:00 – 13:00'),
            ('13:00 – 14:00', '13:00 – 14:00'),
            ('14:00 – 15:00', '14:00 – 15:00'),
            ('15:00 – 16:00', '15:00 – 16:00'),
            ('16:00 – 17:00', '16:00 – 17:00'),
            ('17:00 – 18:00', '17:00 – 18:00'),
        )
        patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
        hospital = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
        date = models.DateField()
        timeslot = models.CharField(choices=TIMESLOT_LIST, default="", max_length=25)
        status = models.BooleanField(default=False)


        def __str__(self):
            return "Patient - {} Doc- {} At {} {} status- {}".format(self.patient, self.hospital, self.date, self.timeslot,self.status)



class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    def __str__(self):
        return self.name



