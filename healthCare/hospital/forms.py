from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from account.models import Patient
from .models import Doctor
from django.forms import ModelForm

class EditPatientProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']

class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'