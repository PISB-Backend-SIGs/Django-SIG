from django.shortcuts import render

def num(request):
    if request.method == 'POST':
        list = []
        num_input = int(request.POST['input'])
        if num_input > 0:
            for i in range (1,num_input + 1):
                list.append(i)
            text = {
                'appended_list':list
            }
        else:
            text = {
                'error':'Kindly enter positive integer'
            }
        return render(request,'number/num.html',text)
    return render(request,'number/num.html')