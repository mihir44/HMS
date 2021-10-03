from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView

from .forms import EditPatientProfile
from account.models import Patient, User, Hospital
from patient.models import Appointment

# Create your views here.
def index(request):
    return render(request, 'hospital/index.html')

def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(instance=request.user)
        return render(request,'hospital/hospital_profile.html', {'name': request.user, 'form':fm})
    else:
        return redirect('/')

def hospital_view_appointment(request):
    appointments = Appointment.objects.filter(hospital=request.user)
    return render(request, 'hospital/appointment.html', {'appointments': appointments})
