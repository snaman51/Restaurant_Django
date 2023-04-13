
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('menu.html',views.men,name="menu"),
    path('index.html', views.index,name="index"),
    path('login.html', views.login,name="login"),
    path('register.html', views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('about.html',views.about,name="about"),
    path('contact.html', views.contact, name="contact"),
    path('add',views.add,name="add"),
    path('cart.html',views.cart,name="cart"),

]