from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import PasswordChange

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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Allready available this gmail')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=fname,
                                                last_name=lname, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Check your password")

    return render(request,'registermain.html')

@login_required()
def myacount(request):
    return render(request,'myaccount.html')

@login_required()
def edit_myacount(request):
    if request.method=="POST":

        user=request.user
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.save()
        return redirect('myapp')

    return render(request,'edit.html')

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        password1=request.POST['password']
        obj=auth.authenticate(username=username,password=password1)
        if obj is not None:
            auth.login(request,obj)
            return redirect("/")
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

@login_required()
def add_to_cart(request,product_id):
    cart=Cart(request)
    cart.add(product_id)
    return render(request,'menu_cart.html')

def cart(request):
    return render(request,'cart.html')

# update our cart increment decrement eg,no.of item our purchase increment price
def update_cart(request, product_id, action):
    cart=Cart(request)

    if action == 'increment':
        cart.add(product_id,1,True)
    else:
        cart.add(product_id,-1,True )
    product = Product.objects.get(pk=product_id)
    quantity=cart.get_item(product_id)['quantity']

    item={
        'product':{
            'id':product_id,
            'name':product.name,
            'image':product.image,
            'price':product.price,
        },
        'total_price':(quantity * product.price)/100,
        'quantity':quantity,
    }

    responce= render(request,'cartslistadd.html',{'item':item})
    responce['HX-Trigger']='update-menu_cart'
    return responce

@login_required(login_url="checkout")
def checkout(request):
    return render(request,'checkout.html')
@login_required(login_url='setpass')
def changepassw(request):
    if request.method=="POST":
        form = PasswordChange(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "password was successfully updated")
        else:
            messages.info(request,"Please check your password")

    form=PasswordChange(user=request.user)
    return render(request,'Changepassword.html', {'form':form})

def hxmenucart(request):
    return render(request,'menu_cart.html')
