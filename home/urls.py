from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views




urlpatterns = [
    path('',views.index,name="index"),
    path('home.html',views.home,name="home"),
    path('home1.html',views.home1,name="home1"),
    path('contact/', views.contact, name="contact"),
    path('about/',views.about, name='About'),
    path('trend/',views.trend, name='Trend'),
    path('proprofile.html',views.Pro_Profile,name="proprofile"),
]