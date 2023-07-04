from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("login",views.Register,name="login"),
    path('loginn',views.login,name='loginn'),
    path('shops',views.shops,name='shops'),
    path("admin",admin.site.urls,name="admin"),


]