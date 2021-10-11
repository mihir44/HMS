from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name
