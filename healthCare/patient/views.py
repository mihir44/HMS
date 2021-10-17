from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, reverse
from django.contrib.auth.forms import UserChangeForm
from .models import Patient_profile, Appointment, Category, Product, Order
from django.contrib import messages
from .forms import EditPatientProfile, Patient_details, AppointmentForm
from django.views import View

from account.models import User, Patient


# Create your views here.

@login_required(login_url='signlog')
def index(request):
    return render(request,'patient/index.html')
@login_required(login_url='plogin')
def profile(request):
    if request.user.is_authenticated:
        fm = EditPatientProfile(request.POST,initial={'username': request.user.username,
                                                  'email': request.user.email})
        profile = Patient_details(request.POST)
        return render(request,'patient/patient_profile.html',
                      {'username': request.user.username,'email':request.user.email, 'form':fm, 'profile': profile})
    else:
        return render(request,'patient_login.html')

@login_required(login_url='signlog')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, 'Aim2Care booked your appointment! Check status in View History')
            return redirect('appointment')
    else:
        initial={'patient':request.user.username}
        print(initial)
        form = AppointmentForm(initial=initial)
    return render(request, 'patient/appointment.html', {'form': form})

def patient_appointment_list(request):
    appointments = Appointment.objects.filter(patient=request.user)
    print(appointments)
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})

def patient_withdraw_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('patient-view-appointment')


@login_required(login_url='signlog')
def lab1(request):
    return render(request, 'patient/lab1.html')


class lab2(View):
    def post(self, request):
        product= request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('lab2')
        
    def get(self, request):
        cart= request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        
        categories = Category.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data={}
        data['products']= products
        data['categories']=categories

        return render(request ,'patient/lab2.html', data)


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_products_by_id(ids)
        return render(request, 'patient/cart.html', {'products' : products})



class CheckOut(View):
    # form_class= OrderForm

    # def form_valid(self,form):
    #     form.send_cust()
    #     return super().form_valid(form)
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.POST.get('pname')
        
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=customer,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            messages.success(request, 'Aim2Care Lab Appointment Booked. Check Your Orders for updates. ')
        request.session['cart'] = {}

        return redirect('cart')

class OrderView(View):
    def get(self , request ):

        orders = Order.objects.filter(customer=request.user)
        print(orders)
    
        # customer = request.session.get('customer')
        # orders = Order.get_orders_by_customer(customer)
        # print(orders)
        return render(request , 'patient/orders.html'  , {'orders' : orders})