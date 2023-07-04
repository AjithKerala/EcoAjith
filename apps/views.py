from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Product
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
        password2=request.POST['passw2']
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
                return redirect('login')
        else:
            messages.info(request,"Check your password")

    return render(request,'Register.html')

def login(request):
    if request.method=="POST":
        emai=request.POST['email']
        password=request.POST['password']
        assign=auth.authenticate(email=emai,password=password)
        if assign is not None:
            auth.login(assign)
            return redirect("/")
        else:
            messages.info(request,"please check your email and password")
    return render(request,'Register.html')


