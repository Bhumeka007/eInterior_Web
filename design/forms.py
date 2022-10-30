from django.forms import ModelForm
from django import forms

from .models import Design
 
# create a ModelForm
# class addDesign(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = Design
        
#         fields = "__all__"
#         widgets={
#             # 'images':forms.ImageField(attrs={'class':'form-control','required':'False'}),
#             'prof':forms.TextInput(attrs={'class':'form-control','required':'True','placeholder':"Dessigner Name"}),
#             #'images':forms.ImageField(attrs={'class':'form-control','required':'False'}),
#             'name':forms.TextInput(attrs={'class':'form-control','required':'True','placeholder':"Design Name"}),
#             #'hotel_price':forms.TextInput(attrs={'class':'form-control','required':'True','placeholder':""}),
#             'description':forms.Textarea(attrs={'class':'form-control','required':'True'}),
#             #'room_count':forms.TextInput(attrs={'class':'form-control','required':'True'}),
#             'tag':forms.TextInput(attrs={'class':'form-control','required':'True'}),
#             #'District':forms.TextInput(attrs={'class':'form-control','required':'True'}),
#         }