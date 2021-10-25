from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from account.models import User

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


class Emergency(models.Model):
        
        ISSUE_LIST = (
            ('Accident', 'Accident'),
            ('Stroke/Attack', 'Stroke/Attack'),
            ('Injury', 'Injury'),
            ('Others', 'Others'),
        )

        NEED_LIST = (
            ('ICU', 'ICU'),
            ('OXYGEN CYLINDER', 'OXYGEN CYLINDER'),
            ('VENTILATOR', 'VENTILATOR'),
        )

        # patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
        pname = models.CharField(default="", max_length=50)
        hospitalsname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dname')
        issue = models.CharField( choices=ISSUE_LIST,default="", max_length=50)
        # email = models.CharField(default="", max_length=25)
        phone = models.CharField(default="", max_length=10)
        requirement = models.CharField(choices=NEED_LIST,default="", max_length=50)
        # bloodgroup = models.CharField( default="", max_length=7)
        # address = models.CharField( default="", max_length=250)
        medicine = models.CharField( default="", max_length=225)
        allergy = models.CharField( default="", max_length=225)
        


        def __str__(self):
            return "Patient - {} Hospital- {} Phone {} ".format(self.pname, self.hospitalsname,self.phone)

