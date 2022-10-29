from django.urls import path
from . import views

urlpatterns = [
    #path('',views.homepage, name='Home'),
    # path("", views.index, name="index"),
    #path('contact/', views.contact, name="contact"),
    #path('sendmail/', views.sendmail, name="sendmail"),
    path("index.html", views.index, name="index1"),

]