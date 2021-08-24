from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    phone = models.CharField(max_length=10, default="")
