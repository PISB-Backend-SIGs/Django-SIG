from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello")
    return render(request,'index.html')

def answerpage(request):
    initial = int(request.GET.get('text','default'))
    text = 'The input value is: '
    if initial>0:
        for i in range(initial):
            text+=str(i)+' '
    else:
        text="Error: the number isnt a natural number"
    params = {'text':text}
    return render(request,'solutions.html',params)