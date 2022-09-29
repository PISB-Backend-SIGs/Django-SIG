
# from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import NewUserForm

from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    return render (request,'base.html')
def Task1(request):
    if request.method == "POST":
        data = request.POST.get('value')
        data2=[]
        if(int(data)<0):
            data3 = -1
            context ={
                'data3':data3,
            }
        else:
            for i in range(1,int(data)+1):
                data2.append(i)
            context ={
                'data2':data2,
            }
        return render(request,"home.html",context)
    return render(request,"home.html")
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            messages.success(request, "Registration successful." )
            return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            
    form = NewUserForm()
    return render (request,"register.html", {"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or passwor.")
    form = AuthenticationForm()
    return render(request,"login.html", context={"login_form":form})