from crispy_forms.layout import Submit, Layout, Field
from django import forms
from datetime import date
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

from .models import Emergency
from account.models import User, Patient, Hospital
from django.forms import ModelForm, widgets, DateInput
import account.models

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(EmergencyForm, self).__init__(*args, **kwargs)
        # self.fields['patient'].queryset = User.objects.filter(is_patient = True)
        self.fields["pname"].label = "Patient's Name"
        self.fields['hospitalsname'].queryset = User.objects.filter(is_hospital = True)
        self.fields["issue"].label = "Select Issue"
        # self.fields["email"].label = "Enter Email ID"
        self.fields["phone"].label = "Enter Phone"
        self.fields["requirement"].label = "What does the Patient need"
        # self.fields["bloodgroup"].label = "Blood Group"
        # self.fields["address"].label = "Address"
        self.fields["medicine"].label = "Is Patient on any medications"
        self.fields["allergy"].label = "Does Patient have any allergy"
        
        # self.helper.add_input(Submit("bookAppointment", "Book your appointment",css_class='btn btn-primary my-3'))

