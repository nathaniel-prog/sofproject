from django import forms
from .models import MyProfile#import the Post model from bemember/models.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PersonForm(forms.ModelForm):
      class Meta:
            model = MyProfile
            fields = ['colorofeyes' ]



class MyUserCreationForm(UserCreationForm):
      class Meta:
            model = User
            fields = ['email','first_name','last_name', 'username']

            widget= {'first_name':forms.TextInput(attrs={'class':'form-control'}),
                     'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'username':forms.TextInput(attrs={'class': 'form-control'}),
                     'last_name':forms.TextInput(attrs={'class':'form-control'})

                     }

