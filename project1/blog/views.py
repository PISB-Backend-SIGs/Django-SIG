from ast import Break
from distutils.log import error
from django.shortcuts import render
from django.http import HttpResponse


def nums(request):
    if request.method == "POST":
        n = int(request.POST["num"])
        l = []
        if n < 0:
            l.append("Enter the Postive number")
            context = {
            'nums': l,
            }
        else:
            for i in range(1, n+1):
                l.append(i)
        context = {
            'nums': l,
        }
        return render(request, "blog/nums.html", context)
    return render(request, "blog/nums.html")
