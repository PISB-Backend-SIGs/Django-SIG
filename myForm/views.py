from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from myForm.models import Post


def index(request):
    return render(request, 'Form.html')

def about(request):
    userid = request.POST.get('Userid')
    fname_ = request.POST.get('fname')
    lname_ = request.POST.get('lname')
    email_ = request.POST.get('email')
    female = request.POST.get('Female')
    male = request.POST.get('Male')
    phone_num = request.POST.get('phone')
    psw = request.POST.get('psw')
    is_user = User.objects.filter(username = userid).exists()
    gndr = ''
    if male=='on':
        gndr = 'M'
    elif female=='on':
        gndr = 'F'
    else:
        gndr = 'U'
    if is_user:
        return render(request,'home.html',{"response":"Already a user please sign in"})
    else:
        User.objects.create(username = userid, password = psw)
        user = User.objects.get(id = 1)
        post = Post(
            name = userid, 
            fname = fname_,
            lname= lname_,
            email= email_,     
            phone= int(phone_num), 
            gender = gndr,
            author = user
            )
        post.save()
        return render(request,'home.html',{"response":"Registeration successful!! please login "})


def register(request):
    p = {"test":"abc"}

    return render(request, 'Successful_login.html',p)

def page(request):
    return render(request, 'home.html')

def home(request):
    user = request.POST.get('username')
    psw = request.POST.get('password')
    print(user,psw)
    is_user = User.objects.filter(username = user).exists()
    if is_user:
        actual_psw = User.objects.get(username = user).password
        if str(actual_psw) == str(psw):
            return render(request, 'Successful_login.html')
        else:
            p = {'response':'please check login id or password'}
            return render(request, 'home.html',p)
    else:
        p = {'response':'Please Register'}
        return render(request, 'home.html',p) 