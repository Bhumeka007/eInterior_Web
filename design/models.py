from django.db import models
from django.contrib.auth.models import *
import uuid

# Create your models here.
class Customer(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    address = models.TextField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.first} {self.last} {self.phone} {self.email} {self.address}"

class Design(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='image/')
    designName = models.CharField(max_length=64, blank=False)              #Which Design
    description = models.CharField(max_length=64, blank=False)    
    tag = models.CharField(max_length=64)                                     

    def __str__(self):
        return f"{self.name} {self.image} {self.designName} {self.description} {self.tag}"

class Card(models.Model):
    cards = models.CharField(max_length=64)                              #Payment way

    def __str__(self):
        return f"Online Payment way {self.cards}"
    
class MethodToPay(models.Model):
    way = models.CharField(max_length=64)      #If it's "Cash on delivery" or "Online Payment"

    def __str__(self):
        return f"Is it {self.way}"
    
class Payment(models.Model):
    Ammount = models.FloatField()               #Total amount
    PaymentWay = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="PaymentMethod")
    UserID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="PaymentAccount")

    def __str__(self):
        return f"{self.UserID} have to pay {self.Ammount} by {self.PaymentWay}"

class Employee(models.Model):
    ProSeName = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    AccountNumber = models.CharField(max_length=32)    #Employee ID

    def __str__(self):
        return f"{self.ProSeName} ({self.phone}) {self.email} {self.AccountNumber}"
    
class Contact(models.Model):
    FullName = models.CharField(max_length=20)
    PhNumber = models.CharField(max_length=20)
    Ema = models.CharField(max_length=32)
    Message = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.FullName} ({self.PhNumber}) {self.Ema} {self.Message}"
    
class addDesign(models.Model):
    prof = models.CharField(max_length=20,null=True,blank=True)
    Name = models.CharField(max_length=20,null=True,blank=True)
    descn =  models.CharField(max_length=150,null=True,blank=True)
    tagi = models.CharField(max_length=15,null=True)

    def __str__(self):
        return f"{self.prof} {self.Name} {self.descn} {self.tagi}"

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
            
class MyDesign(BaseModel):
    design = models.ForeignKey(Design  , related_name="my_dessing" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="pro_design" , on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    tag_des= models.CharField(max_length=10,default="Added")
    
class profileProf(models.Model):
    first_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Phone_Number = models.CharField(max_length=11,null=True)
    mail = models.CharField(max_length=32)
    Project_Type = models.CharField(max_length=40)
    Time = models.FloatField()
    Skills = models.CharField(max_length=50)
    Budget = models.FloatField()
    Company = models.CharField(max_length=32)
    Country = models.CharField(max_length=32)
    
    
    def __str__(self):
        return f"{self.first_Name} {self.Last_Name} {self.Phone_Number} {self.mail} {self.Project_Type} {self.Time} {self.Skills} {self.Budget} {self.Company} {self.Country}"