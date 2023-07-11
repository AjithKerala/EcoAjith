from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from  PIL import Image
from io import BytesIO
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name
class Product(models.Model):
    category=models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    slug=models.SlugField()
    description=models.CharField(max_length=255)
    price=models.IntegerField()
    createdat=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="shop",null=True,blank=True)

    class Meta:
        ordering=('createdat',)
    def __str__(self):
        return self.name
    def priceset(self):
        return self.price/100

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED='shipped'
    STATUS_CHOICE={
        (ORDERED, 'ordered'),
        (SHIPPED,'shipped')


    }
    user=models.ForeignKey(User, related_name='orders',on_delete=models.CASCADE,blank=True,null=True,)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    paid=models.BooleanField(default=False)
    paid_amount=models.IntegerField(default=True,null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default=ORDERED)

class Orderitems(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)


