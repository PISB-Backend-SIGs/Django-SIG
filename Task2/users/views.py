from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re

def register(request):
    message = []
    if request.method == 'POST' :
        newusername = request.POST['newusername']
        mobile = request.POST['Mobile']
        emai_l = request.POST['Email']
        pas = request.POST['Password']
        confirmPassword = request.POST['ConfirmPassword']
        if User.objects.filter(username = newusername).exists() :
            message.append("Username already  Exists")
        elif mobile.isnumeric() == False or len(mobile) != 10 :
            message.append("Enter a valid Mobile number")
        elif  User.objects.filter(email = emai_l).exists():
            message.append("Email is already register")
        elif pas != confirmPassword :
            message.append("Confirmed Password did not match the entered Password")
        if (len(pas) < 8):
             message.append("Password should contain atleast 8 characters")
        elif not re.search("[a-z]", pas):
            message.append("Password should contain atleast one Lowercase letter")
        elif not re.search("[A-Z]", pas):
            message.append("Password should contain atleast one Uppercase letter")
        elif not re.search("[0-9]", pas):
            message.append("Password should contain atleast one Number")
        elif not re.search("[_@#%$]", pas):
            message.append("Password should contain atleast one Special character")
        else :
            message.append("New User created Succesfully")
            User.objects.create_user(username=newusername,password=pas,email=emai_l)
    context = {
        'messages' : message
    }    
    return render(request, 'users/register.html', context)

def content(request):
    return render(request, 'users/content.html')