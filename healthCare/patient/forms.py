from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
import account.models

class EditPatientProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']

# class Patient_details(ModelForm):
#     class Meta:
#         model = Patient_profile
#         fields = '__all__'



