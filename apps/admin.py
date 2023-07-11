from django.contrib import admin
from .models import Category,Product
from  .models import Order
from .models import Orderitems
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitems)