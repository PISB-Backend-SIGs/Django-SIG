from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context={}
    list=[]
    if request.method == 'POST' :
        n=int(request.POST["num"])
        if n<0 :
            list.append("Enter a number greater han Zero")
            context={'num' : list}
        else :
            for i in range (n+1) :
                list.append(i)
                context={'num' : list}

    return render (request,'Core/home.html',context)
