from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'health/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        category = request.POST.get('category','')
        contact = Contact(name = name, email = email, category = category, message = message, phone = phone)
        contact.save()

        messages.success(request, 'Message Sent! Aim2Care will contact you soon')
    return render(request,'health/contact.html')

def patientLogin(request):
    return render(request, 'health/patient_login.html')

def patientRegister(request):
    return render(request, 'health/patient_register.html')

def otp(request):
    return render(request, 'health/otp.html')