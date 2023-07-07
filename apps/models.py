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


