

from django.shortcuts import render,HttpResponse,redirect
from .models import Data  #for Data database
from django.contrib.auth.models import User #for admin user database
from django.contrib.auth import authenticate,login,logout #for authentication system

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #for authentication
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            error=[
                "Username is already taken",
                "Or",
                "Email is already taken",]
            return render(request,'signup.html',{'errors':error})
        else:
            if pass1==pass2:
                #for store in data database
                data=Data(user_name=uname,first_name=fname,last_name=lname,email_id=email,phone_num=phone,
                gender_user=gender,
                password_user=pass1)
                data.save()

                #for store in userdatabase
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save()

                return render(request,'home.html',{'message':"Succesfuly Account Created"})
            else:
                return render(request,'signup.html',{'passmessage':"Passwords are not same"})
                
    else:
        return render(request,'signup.html')

def login_user(request):
    if request.method=="POST":
        usern=request.POST['uname']
        pasword=request.POST['pass']
        user =authenticate(request,username=usern,password=pasword)
        if user is not None:
            login(request,user)
            return render(request,'user.html',{'message':"Succesfuly Loged in",'display':usern})
        else:
            return render(request,'login.html',{'errors':"Invalid Credentials"})
    else:
        return render(request,'login.html')


def user(request):
    return render(request,'user.html')

def check(request):
    if request.method=='POST':
        uname=request.POST['uname']
        if User.objects.filter(username=uname).exists():
            return render(request,'check.html',{'errors':"Username is already taken"})
        else:
            return render(request,'check.html',{'errors':"Congrats Username is available"})
    else:
        return render(request,'check.html')