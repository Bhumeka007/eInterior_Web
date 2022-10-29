from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"eInteriorApp/tamplates/index.html")

@login_required(login_url='login')
def home(request):
    return render(request,"home/tamplate/home.html")

@login_required(login_url='login')
def home1(request):
    return render(request,"home/tamplate/home1.html")

def contact(request):
    return render(request, 'eInteriorApp/tamplates/contact.html')

@login_required(login_url='login')
def about(request):
    return render(request,"home/tamplate/about.html")

@login_required(login_url='login')
def trend(request):
    return render(request,"home/tamplate/trend.html")

def Pro_Profile(request):
    return render(request,"home/tamplate/proprofile.html")
