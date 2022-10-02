import email
from django.shortcuts import render
from .models import NewUser
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.db import IntegrityError

class IncorrectInfoError(Exception):
    pass

def oneUpper(s):
    for i in s:
        if i.isupper():
            return True 
            break
    else:
        return False

def oneLower(s):
    for i in s:
        if i.islower():
            return True 
            break
    else:
        return False

def oneSpecial(s):
    for i in s:
        if i in ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',';',':','?','/','.','>','<',',','~','`',"'",'"',"\\"]:
            return True
            break
    else:
        return False
def printall(k):
    out = []
    if k>0:
        for i in range(1,k+1):
            out.append(i)
        return out
    else:
        return ['Please enter positive number']        
# Create your views here.

def home(request):
    n = int(request.POST.get('num','0'))
    context = {'Num': n ,'func': printall(n)}
    return render(request, "new/base.html",context)

def register(request):
    error = []
    try:
        if request.method == "POST":
            user = NewUser.objects.create_user(username=request.POST.get('username'),
            email=request.POST.get('email'),
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            phone_num=request.POST.get('phonenumber'),
            gender = request.POST.get('gender'))
            user.set_password(request.POST.get('password'))
            
            if len(NewUser.objects.last().phone_num)!=10 :
                error.append("Phone number should be 10 digit")
                raise IncorrectInfoError()


            for userobj in NewUser.objects.all():
                if userobj == NewUser.objects.last():
                    continue
                if userobj.email == user.email:
                    error.append("Email already linked to another username.")
                    raise IncorrectInfoError()
                    break
            for userobj in NewUser.objects.all():
                if userobj == NewUser.objects.last():
                    continue
                if userobj.phone_num == user.phone_num:
                    error.append("Phone Numbers already linked to another username.")
                    raise IncorrectInfoError()
                    break
            if not check_password(request.POST.get('confirmpass'),user.password):
                error.append('Passwords not matching.')
                raise IncorrectInfoError()
            
            if not ((len(request.POST.get('password')) > 8) and ( oneUpper(request.POST.get('password'))) and (oneLower(request.POST.get('password'))) and (oneSpecial(request.POST.get('password')))) :
                error.append("Password must contain atleast 8 digits. Must contain atleast 1 upper case letter, 1 lower case letter and a speciual character.")
                raise IncorrectInfoError()
            
    except IntegrityError:
        error.append("Username already taken.")
    except IncorrectInfoError:
        user.delete()

    
    context = {"error": error,}
    
    return render(request,"new/register.html",context)