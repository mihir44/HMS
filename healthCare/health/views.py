from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Contact, Emergency
from .forms import EmergencyForm
from django.views import View
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
        # email = EmailMessage()
        # send_mail(
        #     category, # subject
        #     message, # message
        #     email, # from email
        #     ['aim2care29@gmail.com'], # to email
        # )
        messages.success(request, 'Message Sent! Aim2Care will contact you soon')
    return render(request,'health/contact.html')

def otp(request):
    return render(request, 'health/otp.html')


def about(request):
    return render(request, 'health/about.html')


def signlog(request):
    return render(request, 'health/signlog.html')


def emergencyhosp(request):
    return render(request, 'health/emergencyhosp.html')



def emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST)
        if form.is_valid():
            Emergency = form.save(commit=False)
            Emergency.save()
            messages.success(request, 'Emergency Request Done!')
            return redirect('emergency')
    else:
        initial={'patient':request.user.username}
        print(initial)
        form = EmergencyForm(initial=initial)
    return render(request, 'health/emergency.html', {'form': form})
