from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import EditPatientProfile

# Create your views here.
def index(request):
    return render(request, 'hospital/index.html')

def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(instance=request.user)
        return render(request,'hospital/hospital_profile.html', {'name': request.user, 'form':fm})
    else:
        return redirect('/')