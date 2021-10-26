from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_patient:
            return redirect('patient_home')
        elif request.user.is_authenticated and request.user.is_hospital:
            return redirect('hospital_home')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

def allowed_user(allowed_role = []):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_role:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("You are not authorized to this page")
        return wrapper_func
    return decorator