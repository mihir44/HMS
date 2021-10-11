from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, reverse
from django.contrib.auth.forms import UserChangeForm
from .models import Appointment
from django.contrib import messages
from .forms import EditPatientProfile, Patient_details, AppointmentForm


# Create your views here.

@login_required(login_url='signlog')
def index(request):
    return render(request,'patient/index.html')
@login_required(login_url='plogin')
def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(request.POST,initial={'username': request.user.username,
                                                  'email': request.user.email})
        profile = Patient_details(request.POST)
        return render(request,'patient/patient_profile.html',
                      {'username': request.user.username,'email':request.user.email, 'form':fm, 'profile': profile})
    else:
        return render(request,'patient_login.html')

@login_required(login_url='signlog')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, 'Aim2Care booked your appointment! Check status in View History')
            return redirect('appointment')
    else:
        form = AppointmentForm()
    return render(request, 'patient/appointment.html', {'form': form})

def patient_appointment_list(request):
    appointments = Appointment.objects.filter(patient=request.user)
    print(appointments)
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})

def patient_withdraw_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('patient-view-appointment')


@login_required(login_url='signlog')
def lab1(request):
    return render(request, 'patient/lab1.html')

def lab2(request):
    return render(request, 'patient/lab2.html')
