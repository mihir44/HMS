from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Patient,Hospital
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        def save(self,commit=True):
            user = super().save(commit=True)
            user.email = self.cleaned_data('email')
            user.first_name = self.cleaned_data('first_name')
            user.last_name = self.cleaned_data('last_name')
            if commit:
                user.save()
                return user

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['gender','phone_number','address','city','state','postal','dob']
