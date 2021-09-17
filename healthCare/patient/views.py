from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from .forms import EditPatientProfile
# Create your views here.
def index(request):
    return render(request,'patient/index.html')

def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(instance=request.user)
        return render(request,'patient/patient_profile.html', {'name': request.user, 'form':fm})
    else:
        return render(request,'patient_login.html')
