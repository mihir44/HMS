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

# def patientDetails(request):
#     patient = request.user.user
#     form = Patient_details(instance=patient)
#
#     if request.method == 'POST':
#         form = Patient_details(request.POST, request.FILES, instance=patient)
#         if form.is_valid():
#             form.save()

    context = {'form': form}
    return render(request, 'accounts/accounts_setting.html', context)