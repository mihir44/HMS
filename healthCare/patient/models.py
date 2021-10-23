from django.db import models
from account.models import Patient, Hospital,User
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

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

        ISSUE_LIST = (
            ('Routine Checkup', 'Routine Checkup'),
            ('Major Health Issues', 'Major Health Issues'),
            ('Joint Muscle Issues', 'Joint Muscle Issues'),
            ('Hormonal Imbalance', 'Hormonal Imbalance'),
            ('Infections and rashes', 'Infections and rashes'),
        )

        DOCTOR_LIST = (
            ('Dr. Abhishek Wadkar - Routine Checkup', 'Dr. Abhishek Wadkar - Routine Checkup'),
            ('Dr. Meheka Sheikh - Routine Checkup', 'Dr. Meheka Sheikh - Routine Checkup'),
            ('Dr. Arvind Sagota - Routine Checkup', 'Dr. Arvind Sagota - Routine Checkup'),
            ('Dr. Meenal Shah - Routine Checkup', 'Dr. Meenal Shah - Routine Checkup'),
            ('Dr. Adrik Kaif - Routine Checkup', 'Dr. Adrik Kaif - Routine Checkup'),

            ('Dr. Manpreet Singh - Major Health Issues', 'Dr. Manpreet Singh - Major Health Issues'),
            ('Dr. Jay Sarkar - Major Health Issues', 'Dr. Jay Sarkar - Major Health Issues'),
            ('Dr. Aisha Manila - Major Health Issues', 'Dr. Aisha Manila - Major Health Issues'),
            ('Dr. Ketan Jha - Major Health Issues', 'Dr. Ketan Jha - Major Health Issues'),
            ('Dr. Murkh Injam - Major Health Issues', 'Dr. Murkh Injam - Major Health Issues'),
            
            ('Dr. Ashwin Mehta - Joint Muscle Issues', 'Dr. Ashwin Mehta - Joint Muscle Issues'),
            ('Dr. Keith Sequira - Joint Muscle Issues', 'Dr. Keith Sequira - Joint Muscle Issues'),
            ('Dr. Camil Dcruz - Joint Muscle Issues', 'Dr. Camil Dcruz - Joint Muscle Issues'),
            ('Dr. Jaya Deshmukh - Joint Muscle Issues', 'Dr. Jaya Deshmukh - Joint Muscle Issues'),
            ('Dr. Mandira Chopda - Joint Muscle Issues', 'Dr. Mandira Chopda - Joint Muscle Issues'),

            ('Dr. Aksa Pradhan - Hormonal Imbalance', 'Dr. Aksa Pradhan - Hormonal Imbalance'),
            ('Dr. Hritika Doshi - Hormonal Imbalance', 'Dr. Hritika Doshi - Hormonal Imbalance'),
            ('Dr. Misha mishra - Hormonal Imbalance', 'Dr. Misha mishra - Hormonal Imbalance'),
            ('Dr. Meetal Manoja - Hormonal Imbalance', 'Dr. Meetal Manoja - Hormonal Imbalance'),
            ('Dr. Akash Wadvani - Hormonal Imbalance', 'Dr. Akash Wadvani - Hormonal Imbalance'),

            ('Dr. Prem Singhania - Infections and rashes', 'Dr. Prem Singhania - Infections and rashes'),
            ('Dr. Kabeer Hongal - Infections and rashes', 'Dr. Kabeer Hongal - Infections and rashes'),
            ('Dr. Priya Narwande - Infections and rashes', 'Dr. Priya Narwande - Infections and rashes'),
            ('Dr. Lalita Sangikar - Infections and rashes', 'Dr. Lalita Sangikar - Infections and rashes'),
            ('Dr. Aditi Surekh - Infections and rashes', 'Dr. Aditi Surekh - Infections and rashes'),
            
        )

        # patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
        patient = models.CharField(default="", max_length=50)
        hospital = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
        coursecategory = models.CharField( choices=ISSUE_LIST,default="", max_length=50)
        coursetopic = models.CharField(choices=DOCTOR_LIST,default="", max_length=50)
        date = models.DateField(null=True, blank=True, default=None, validators=[validate_date])
        timeslot = models.CharField(choices=TIMESLOT_LIST, default="", max_length=25)
        status = models.BooleanField(default=False)


        def __str__(self):
            return "Patient - {} Doc- {} At {} {} Doctor Name {} status- {}".format(self.patient, self.hospital, self.date,self.coursetopic, self.timeslot,self.status)



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
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.CharField(max_length=50, default='', blank=True)
                                 
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    pname = models.CharField(max_length=50, default='', blank=True)
    dname = models.CharField(max_length=50, default='', blank=True)
    labtime = (
        ('08:00 – 09:00', '08:00 – 09:00'),
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
    labtime = models.CharField(max_length=25, choices=labtime, default="labtime")
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    # @staticmethod
    # def get_orders_by_customer(user):
    #     return Order.objects.filter(customer=user).order_by('-date')



