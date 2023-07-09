from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path('login',views.login,name='login'),
    path('register',views.Register,name="register"),
    path('logout',views.logout,name='logout'),
    path('myapp',views.myacount,name='myapp'),
    path('shops',views.shops,name='shops'),
    path('product/<slug:slug>/',views.products, name='product'),
    path('addtocart/<int:product_id>/',views.add_to_cart,name='addtocart'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('setpass',views.changepassw,name='setpass'),
    path("admin",admin.site.urls,name="admin"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)