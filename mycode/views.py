from multiprocessing import context
from socket import fromshare
from unittest.util import _MAX_LENGTH
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django import forms


def home(request):
    list1 = []
    context = {}

    if request.method == 'POST':
        n = int(request.POST['n'])
        if n > 0:
            for i in range(1, n+1):
                list1.append(i)
            context = {'Number':list1}
            
        else:
            list1.append("Enter a number greater than Zero")
            context={'Number':list1}
    return render(request, "mycode/base.html", context)
