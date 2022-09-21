from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint

def Kuchbhi(request):
    dict = {
        'title': 'SHOW THIS',
        'newdata': 'HELLO HTML!',
        'clist': ['css', 'html', 'javascript']
    }

    return render(request, "index.html", dict)


def shinchan(request):
    return HttpResponse("hi im sid.")





def Userform(request):
    ans=[]

    try:
        n1 = int(request.GET['num1'])
        for i in range(1, n1 + 1):
            ans.append(i)



    except:
        pass
    return render(request, "counting.html" , {'output': ans})
