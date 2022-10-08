from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):

    place= models.IntegerField()
    ques = models.CharField(max_length=100)

    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)

    ans = models.CharField(max_length=100)

    


    # for table name
    def __str__(self):
        return self.ques

class Credential(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number =models.IntegerField()
    crntque =models.IntegerField()
    marks =models.IntegerField()
    trys=models.IntegerField()

    def __str__(self):
        return self.user.username

