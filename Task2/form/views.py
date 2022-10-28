from django.shortcuts import render
from .form import UserRegisterForm
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            form.save()
    else:
        form = UserRegisterForm()
    return render(request,'blog/home.html', {'form': form })