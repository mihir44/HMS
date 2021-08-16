from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("home page")

def contact(request):
    if request.method == 'POST':
        print(request)
    return render(request,'health/contact.html')