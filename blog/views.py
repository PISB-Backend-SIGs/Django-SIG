from django.shortcuts import render

# this function will handle the traffic from the homepage of our blog
# it will take a request argument. Here we're simply going to return what  we want 
# the user to see when they're sent to this route
def home(request): 
    return render(request, 'blog/home.html') 

def nos(request):

    if ( request.method == "POST"):
        val = int(request.POST['num1'])
        s = ""
        if val >= 0:
            for i in range(1, val+1):
                s = s + str(i)
        else:
            s = "Enter valid request"

        

    return render(request, 'blog/result.html', {'val': s})