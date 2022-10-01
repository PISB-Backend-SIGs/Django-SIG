from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.TextField(default='no name')
    fname = models.TextField(default='no fname')
    lname = models.CharField(max_length=100, default='no lname')
    email = models.EmailField(default='no email')
    phone = models.TextField(max_length=10, default=-1)
    gender = models.CharField(max_length=1, default='U')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
