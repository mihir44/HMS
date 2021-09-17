from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from account.models import Patient

class EditPatientProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']