from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse

from django.db.models import Q
from .forms import *
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def homepage(request):
    user = Customer.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()
    
    if request.method == 'POST':
        fullname = request.POST.get('flname')
        phnum = request.POST.get('phname')
        Email = request.POST.get('ceml')
        message = request.POST.get('mess')
        
        # Contact.objects.create(FullName=fullname, PhNumber=phnum, Ema=Email, Message=message)
        # messages.success("Your query was sent")
        # return redirect('Home')
        
        # subject = 'welcome to eInterior'
        # messages = [message]
        # email_from = settings.EMAIL_HOST_USER
        # email =[Email]
        # send_mail(subject,messages,email_from,email)
        
        Mydata = Contact()
        Mydata.FullName=fullname
        Mydata.PhNumber=phnum
        Mydata.Ema=Email
        Mydata.Message=message
        
        Mydata.save()
        
        print(request.POST)

    context = {
        'Users': user,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'eInteriorApp/tamplates/index.html', context)

def contacts(request):
    Contacts = Contact.objects.all()
    context={
        "messege":Contacts
    }
    return render(request, 'eInteriorApp/tamplates/contact.html', context)

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


def professionalpage(request):
    if request.method == 'POST':
        professionalname = request.POST.get('pname')
        AccountNum = request.POST.get('paccnum')
        PhoneNum = request.POST.get('pphnum')
        Email = request.POST.get('peml')

        Mydata = Employee()
        Mydata.ProSeName=professionalname
        Mydata.AccountNumber=AccountNum
        Mydata.phone=PhoneNum
        Mydata.email=Email

        Mydata.save()

    return render(request, 'home/tamplate/professional.html')

def aboutpage(request):
    return render(request, 'home/tamplate/about.html')

def ProProfile(request):
     if request.method == 'POST':
        
         ProfFName =  request.POST.get('pffname')
         ProfLName =  request.POST.get('pflname')
         phnumbers = request.POST.get('pfphnum')
         Mail =  request.POST.get('pfeml')
         Ptype =  request.POST.get('pfpt')
         Tm =  request.POST.get('pft')
         skl =  request.POST.get('pfs')
         Bdg =  request.POST.get('pfb')
         Comp =  request.POST.get('pfc')
         Cntry =  request.POST.get('pfct')

         Mydata = profileProf()
         Mydata.first_Name = ProfFName
         Mydata.Last_Name = ProfLName
         Mydata.Phone_Number = phnumbers
         Mydata.mail = Mail
         Mydata.Project_Type = Ptype
         Mydata.Time = Tm
         Mydata.Skills = skl
         Mydata.Budget = Bdg
         Mydata.Company = Comp
         Mydata.Country = Cntry

         Mydata.save()
         print(request.POST)
        

     return render(request, 'eInteriorApp/tamplates/index.html')
#     return render(request, 'profile.html')
#  Tanah Part Start
def RoomDesign(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'roomDesign.html', context)

def PlantsAtoZ(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'plantsAtoZ.html', context)

def Decorating(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'decorating.html', context)

def Designing(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'designStyle.html', context)

def Small(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'smallSpace.html', context)

def Out(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'outDoor.html', context)

def Ind(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'inDoor.html', context)

def Skl(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'skills.html', context)

def Cln(request):
    desg = Design.objects.all()
    DesigCat = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    Py = Payment.objects.all()

    context = {
        'Designs': desg,
        'DesignCatalog': DesigCat,
        'PaymentWay': WayPay,
        'Pay': Py,
    }

    return render(request, 'clen.html', context)

#  Tanah Part end
def AddDesign(request):
    if request.method == 'POST':
        fullname = request.POST.get('pf')
        phnum = request.POST.get('nm')
        Email = request.POST.get('ds')
        message = request.POST.get('tge')
        
        # Contact.objects.create(FullName=fullname, PhNumber=phnum, Ema=Email, Message=message)
        # messages.success("Your query was sent")
        # return redirect('Home')
        
        # subject = 'welcome to eInterior'
        # messages = [message]
        # email_from = settings.EMAIL_HOST_USER
        # email =[Email]
        # send_mail(subject,messages,email_from,email)
        
        Mydata = addDesign()
        Mydata.prof=fullname
        Mydata.Name=phnum
        Mydata.descn=Email
        Mydata.tagi=message
        
        Mydata.save()
        
        print(request.POST)
        return redirect('mydesign')
    # context ={}
 
    # # create object of form
    # form1 = addDesign(request.POST , request.FILES )
    # # if request.method=="POST":
    # # check if form data is valid
    
    # if form1.is_valid():
    #     # save the form data to model
    #         form1.save()
    #         messages.success(request,'Succecfully Added')
    #         return redirect('add design')
    
    
    # context['form']= form1
    return render(request, "addDesign.html")

@login_required(login_url='login')
def MYDesign(request):
    
    My_Design = addDesign.objects.filter()
    context={
         "My_Design":My_Design,
    }
   
    return render(request,"mydesign.html",context)
