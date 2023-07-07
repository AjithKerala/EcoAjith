from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("login",views.Register,name="login"),
    path('loginn',views.login,name='loginn'),
    path('shops',views.shops,name='shops'),
    path('products/<slug:slug>/',views.products, name='products'),
    path('addtocart/<int:product_id>/',views.add_to_cart,name='addtocart'),
    path("admin",admin.site.urls,name="admin"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)