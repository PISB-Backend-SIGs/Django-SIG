from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your models here.
class NewUser(User):
    # list_display = ('username', 'email', 'first_name', 'last_name')
    phone_num = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=15, null=True)
