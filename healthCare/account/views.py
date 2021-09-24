from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User,Patient,Hospital
from .decoraters import unauthenticated_user

# Create your views here.
@unauthenticated_user
def pregister(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        phone_number = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('pregister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('pregister')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name,is_patient = True)
                user.save()
                user_name = User.objects.filter(username=username)[0]
                patient = Patient.objects.create(user=user_name, phone_number=phone_number)
                patient.save()
                return redirect('plogin')
        else:
            messages.info(request, 'password not matching..')
            return redirect('pregister')
    else:
        return render(request, 'patient_register.html')

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
