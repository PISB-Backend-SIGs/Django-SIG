from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    phone_Number= forms.CharField(max_length=10, required=True, help_text='Phone number')
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username",'first_name', 'last_name','phone_Number', "email", "password1", "password2"]
