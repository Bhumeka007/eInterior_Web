from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import *
# from django.core.mail import send_mail
# from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"eInteriorApp/tamplates/index.html")
# def contact(request):
#     return render(request, 'eInteriorApp/tamplates/contact.html')

# def sendmail(request):
#     if request.method == 'POST':
#         fullname = request.POST.get('flname')
#         phnum = request.POST.get('phname')
#         Email = request.POST.get('ceml')
#         message = request.POST.get('mess')
#         send_mail(
#         fullname,
#         phnum,
#         Email,
#         message, 
#         'eInterior007@gmail.com',
#         ['19101026@uap-bd.edu'],
#         fail_silently=False,
#         )
#         messages.info(request, "Mail send successfully")
#         return render(request, 'eInteriorApp/tamplates/contact.html')
#     else:
#         messages.info(request, "Mail didn't send because of some error")
#         return render(request, 'eInteriorApp/tamplates/contact.html')


@login_required(login_url='login')
def home(request):
    return render(request,"eInterior/home.html")

@login_required(login_url='login')
def about(request):
    return render(request,"eInterior/about.html")