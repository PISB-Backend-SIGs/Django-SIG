

from django.shortcuts import render,HttpResponse,redirect
from .models import Data  #for Data database
from django.contrib.auth.models import User #for admin user database
from django.contrib.auth import authenticate,login,logout #for authentication system
import re

#django admin panel
#   Prasad
#   Prasad@2003

# Create your views here.
def home(request):
    return render(request,'home.html')

#for signup 
def signup(request):
    error=[]
    ct=0
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
    
    

        #for authentication and errors
        if len(phone)!=10:
            error.append("Wrong phone number")
            ct+=1
        if  User.objects.filter(email=email).exists():
            error.append("Email is already register")
            ct+=1
        if Data.objects.filter(phone_num=phone):
            error.append("Phone is already register")
            ct+=1
        if User.objects.filter(username=uname).exists() :
            error.append("Username is already register")
            ct+=1
        if (ct>=1):
            return render(request,'signup.html',{'errors':error})
   
        else:
            if pass1==pass2 :
                if len(pass1)>=8:
                    regex="(?=.*[a-z])(?=.*[A-Z])(?=.*[1-9])(?=.*[&@#$%])"
                    patt=re.search(regex,pass1)
                    if patt:
                        #for store in data database
                        data=Data(user_name=uname,first_name=fname,last_name=lname,email_id=email,phone_num=phone,
                        gender_user=gender,
                        password_user=pass1)
                        data.save()
                        #for store in userdatabase
                        user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                        user.save()

                        return render(request,'home.html',{'message':"Succesfuly Account Created"})                    

                        # special =["@","#","_"]
                        # a=0
                        # d=0
                        # s=0
                        # c=0
                        # if len(pass1)>=8:
                        #     for i in pass1:
                        #         if i.isupper():
                        #             c+=1
                        #         if i.isalpha():
                        #             a+=1
                        #         if i.isnumeric():
                        #             d+=1
                        #         if i in special:
                        #             s+=1
                        # if a>=1 and d>=1 and s>=1 and c>=1:
                        #     #for store in data database
                        #     data=Data(user_name=uname,first_name=fname,last_name=lname,email_id=email,phone_num=phone,
                        #     gender_user=gender,
                        #     password_user=pass1)
                        #     data.save()

                        #     #for store in userdatabase
                        #     user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                        #     user.save()

                        #     return render(request,'home.html',{'message':"Succesfuly Account Created"})
                    else :

                        passmessage="Password should be atleast 8 digit \n It must contain atlest 1 uppercase character \n atleast 1 lowercase character \n atlest one special character"
                        return render(request,'signup.html',{'passmessage':passmessage})
                else :
                    # print ("password should be greater than 7 character")
                    return render(request,'signup.html',{'passmessage':"password should be greater than 7 character"})
                
            else:
                return render(request,'signup.html',{'passmessage':"Passwords are not same"})
                
    else:
        return render(request,'signup.html')


#for login 
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

#for logout
def logout_user(request):
    logout(request)
    return render(request,'home.html')

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