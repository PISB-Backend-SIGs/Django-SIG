from django.shortcuts import render

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
