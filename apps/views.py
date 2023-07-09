from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart

from .models import Product, Category


# Create your views here.
def Home(request):
    data={'value':Product.objects.all}
    return render(request,'home.html',data)
def Register(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['passw1']
        password2=request.POST['passwtwo']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Allready Available this username")
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Allready available this gmail')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=fname,
                                                last_name=lname, email=email)
                user.save()
                return redirect('register')
        else:
            messages.info(request,"Check your password")

    return render(request,'registermain.html')

def login(request):
    if request.method=="POST":
        mail=request.POST['email']
        password1=request.POST['password']
        obj=auth.authenticate(email=mail,password=password1)
        if obj is not None:
            auth.login(request,obj)
            return render("/")
        messages.info(request,'please check your mail and password')


    return render(request,'Register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def  shops(request):
    category=Category.objects.all()
    data =Product.objects.all()
    active_category=request.GET.get("category",'')
    if active_category:
        data =Product.objects.filter(category__slug=active_category)
    query=request.GET.get('query','')
    if query:
        data =Product.objects.filter (Q(name__contains=query) |Q(description__contains=query))



    return render(request,'shop.html',{'data':data,'category':category,'active_category':active_category})
def products(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request,'products.html',{"product":product})


def add_to_cart(request,product_id):
    cart=Cart(request)
    cart.add(product_id)
    return render(request,'menu_cart.html')

def cart(request):
    return render(request,'cart.html')

@login_required
def checkout(request):
    return render(request,'checkout.html')