from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView
from health.models import Emergency
from patient.forms import AppointmentForm
from patient import views as p_view
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

def hospital_approve_appointment(request,pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.status = True
    appointment.save()
    return redirect(reverse('doctor-view-appointment'))


def hospital_delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('doctor-view-appointment')




# EMERGENCY

def hospital_view_emergency(request):
    emergency = Emergency.objects.filter(hospitalsname=request.user)
    return render(request, 'hospital/emergencybook.html', {'emergency': emergency})

# def hospital_approve_emergency(request,pk):
#     emergency = Emergency.objects.get(id=pk)
#     emergency.status = True
#     emergency.save()
#     return redirect(reverse('dname-view-emergency'))


# def hospital_delete_emergency(request, pk):
#     emergency = Emergency.objects.get(id=pk)
#     emergency.delete()
#     return redirect('dname-view-emergency')

