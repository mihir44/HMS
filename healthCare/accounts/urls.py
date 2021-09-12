from django.urls import path,include
from . import views

urlpatterns = [
    path('pregister/', views.pregister, name='pregister'),
    path('plogin/',views.plogin, name='plogin'),
    path('hregister/', views.hregister, name='hregister'),
    path('hlogin/',views.hlogin, name='hlogin'),
    path('logout/', views.logout, name='logout'),
]