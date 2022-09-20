from django.shortcuts import render

def printall(k):
    out = []
    if k>0:
        for i in range(1,k+1):
            out.append(i)
        return out
    else:
        return ['Enter positive number only']        
# Create your views here.
def home(request):
    n = int(request.GET.get('num','0'))
    context = {'Num': n ,'func': printall(n)}


    return render(request, "core/base.html",context)