from cProfile import label
from tkinter import Label, Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import form 

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=True, help_text='Phone number')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone','email','password1','password2'] 
        

