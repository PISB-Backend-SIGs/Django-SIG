from django.db import models

# Create your models here.
class Data(models.Model):
    user_name=models.CharField(max_length=15)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=100)
    gender_user=models.CharField(max_length=15)
    password_user=models.CharField(max_length=100)
