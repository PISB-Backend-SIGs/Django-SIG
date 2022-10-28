from email.policy import default
from django.db import models
from .form import UserRegisterForm
from .form import UserCreationForm


class User(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Mobile = models.TextField(max_length=10, blank='false')
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
