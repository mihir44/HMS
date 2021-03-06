from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,reverse
from health.models import Emergency
from .forms import EditPatientProfile,DoctorsForm
from patient.models import Appointment
from django.contrib import messages
from .models import Doctor
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='signlog')
def index(request):
    return render(request, 'hospital/index.html')

@login_required(login_url='signlog')
def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(instance=request.user)
        return render(request,'hospital/hospital_profile.html', {'name': request.user, 'form':fm})
    else:
        return redirect('/')


@login_required(login_url='signlog')
def hospital_view_appointment(request):
    appointments = Appointment.objects.filter(hospital=request.user)
    return render(request, 'hospital/appointment.html', {'appointments': appointments})

@login_required(login_url='signlog')
def hospital_approve_appointment(request,pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.status = True
    appointment.save()
    return redirect(reverse('doctor-view-appointment'))


@login_required(login_url='signlog')
def hospital_delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('doctor-view-appointment')

@login_required(login_url='signlog')
def doctor_add_view(request):
    if request.method == 'POST':
        form = DoctorsForm(request.POST,request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            messages.success(request, 'Doctor details added successfully')
            return redirect('hospital_home')
    else:
        initial={'hospital':request.user.username}
        form = DoctorsForm(initial=initial)
    return render(request, 'hospital/doctorAdd.html', {'form': form})

@login_required(login_url='signlog')
def doctor_list_view(request):
    doctor = Doctor.objects.filter(hospital=request.user)
    return render(request, 'hospital/doctorList.html', {'doctor': doctor})

@login_required(login_url='signlog')
def hospital_delete_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('doctor_list')
# EMERGENCY

@login_required(login_url='signlog')
def hospital_view_emergency(request):
    emergency = Emergency.objects.filter(hospitalsname=request.user)
    return render(request, 'hospital/emergencybook.html', {'emergency': emergency})


