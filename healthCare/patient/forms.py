from crispy_forms.layout import Submit, Layout, Field
from django import forms
from datetime import date
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

from .models import Patient_profile, Appointment, Order
from account.models import User, Patient, Hospital
from django.forms import ModelForm, widgets, DateInput
import account.models

class EditPatientProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class Patient_details(ModelForm):
    class Meta:
        model = Patient_profile
        fields = ('address','city','state','postal','dob','medical_history','gender')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date' : DateInput(attrs={'type': 'date'})
        }


    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # self.fields['patient'].queryset = User.objects.filter(is_patient = True)
        self.fields['hospital'].queryset = User.objects.filter(is_hospital = True)
        self.fields["coursecategory"].label = "Select Issue"
        self.fields["coursetopic"].label = "Select Doctor"
        self.fields["date"].label = "Date (YYYY-MM-DD)"
        self.fields["timeslot"].label = "Time 24 hr (HH:MM)"
        self.fields["status"].widget = forms.HiddenInput()
        # self.helper.add_input(Submit("bookAppointment", "Book your appointment",css_class='btn btn-primary my-3'))

# class OrderForm(forms.Form):
#     customer=forms.CharField()
    
#     class Meta:
#         model = Order
#         fields = ('customer',)
        # widgets = {
        #     'date' : DateInput(attrs={'type': 'date'})
        # }


    # def __init__(self, *args, **kwargs):
    #     super(AppointmentForm, self).__init__(*args, **kwargs)
    #     # self.fields['patient'].queryset = User.objects.filter(is_patient = True)
    #     self.fields['hospital'].queryset = User.objects.filter(is_hospital = True)
    #     self.fields["coursecategory"].label = "Select Issue"
    #     self.fields["coursetopic"].label = "Select Doctor"
    #     self.fields["date"].label = "Date (YYYY-MM-DD)"
    #     self.fields["timeslot"].label = "Time 24 hr (HH:MM)"
    #     self.fields["status"].widget = forms.HiddenInput()
    #     # self.helper.add_input(Submit("bookAppointment", "Book your appointment",css_class='btn btn-primary my-3'))



