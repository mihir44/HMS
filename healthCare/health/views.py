from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import Product
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

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
        send_mail(
            category, # subject
            message, # message
            email, # from email
            ['aim2care29@gmail.com'], # to email
        )
        messages.success(request, 'Message Sent! Aim2Care will contact you soon')
    return render(request,'health/contact.html')

def otp(request):
    return render(request, 'health/otp.html')


def about(request):
    return render(request, 'health/about.html')


@login_required(login_url='signlog')
def lab1(request):
    return render(request, 'health/lab1.html')


@login_required(login_url='signlog')
def lab2(request):
    prds = Product.get_all_products()
    return render(request, 'health/lab2.html', {'products' : prds})


@login_required(login_url='signlog')
def lab3(request):
    return render(request, 'health/lab3.html')

def signlog(request):
    return render(request, 'health/signlog.html')


    