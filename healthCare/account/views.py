from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User,Patient,Hospital
<<<<<<< HEAD
from .decoraters import unauthenticated_user

=======
from .forms import Patient_form,UserForm
>>>>>>> 47bc73da4dd6665836b0b17418d066c55bd9b616
# Create your views here.
@unauthenticated_user
def pregister(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        patient = Patient_form(request.POST)
        if form.is_valid() and patient.is_valid():
            user = form.save()
            patient = Patient_form.save(commit=False)
            patient.user=user
            patient.save()
            return redirect('plogin')
    else:
        form = UserForm(request.POST)
        patient = Patient(request.POST)
    context = {'form': form, 'patient': patient}
    return render(request,'patient_register.html', context)


@unauthenticated_user
def plogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password, is_patient = True)

        if user is not None:
            auth.login(request, user)
            return redirect("/patient")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('plogin')

    else:
        return render(request, 'patient_login.html')

@unauthenticated_user
def hregister(request):
    if request.method == 'POST':
        username = request.POST['hname']
        phone_number = request.POST['mobile']
        password1 = request.POST['password']
        password2 = request.POST['password-repeat']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'account already created')
                return redirect('hregister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('hregister')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,is_hospital = True)
                user.save()
                user_name = User.objects.filter(username=username)[0]
                hospital = Hospital.objects.create(doctor=user_name, phone_number=phone_number)
                hospital.save()
                return redirect('hlogin')
        else:
            messages.info(request, 'password not matching..')
            return redirect('hregister')

    else:
        return render(request, 'hospital_register.html')

@unauthenticated_user
def hlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # hospital = auth.authenticate(email=email, password=password, is_hospital = True)
        hospital = auth.authenticate(username=username, password=password, is_hospital = True)
        if hospital is not None:
            auth.login(request, hospital)
            return redirect("/hospital")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('hlogin')
    else:
        return render(request, 'hospital_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
