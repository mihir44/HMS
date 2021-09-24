from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from .forms import EditPatientProfile, Patient_details, AppointmentForm


# Create your views here.

@login_required(login_url='plogin')
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

@login_required(login_url='plogin')
def appointment(request):
    form = AppointmentForm(request.POST)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'patient/appointment.html',context)
