from django.shortcuts import render

def number(request):
    if request.method=='POST':
        stored_value = int(request.POST['user_value'])
        data = []
        for_negative = 'Enter a valid no.'
        if stored_value<0:
            context={
                'for_negative':for_negative
            }
        else:
            for i in range (1,stored_value+1):
                data.append(i)
            context={
                'data':data
            }
        return render(request,'taskapp/number.html',context)
    return render(request,'taskapp/number.html')