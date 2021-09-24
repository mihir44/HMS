from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_patient:
            return redirect('patient_home')
        elif request.user.is_authenticated and request.user.is_hospital:
            return redirect('hospital_home')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func