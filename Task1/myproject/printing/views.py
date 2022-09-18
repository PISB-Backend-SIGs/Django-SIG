from unittest import result
from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    if request.method=='POST':
        num =int(request.POST['num'])
        # print(URL)
        if (num==0):
            op="Enter Number Greater Than 0"
            return render(request,'html/index.html',{'op':op})
        else :
            result=[]
            for i in range (1,num+1):
                result.append(i)

        return render(request,'html/index.html',{'result':result})
    else :
        return render(request,'html/index.html')
    
