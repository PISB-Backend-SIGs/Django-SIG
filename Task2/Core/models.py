from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    def __str__(self):
        return self.Title