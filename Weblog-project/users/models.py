from typing import Iterable, Optional
from django.db import models

from django.contrib.auth.models import User

from PIL import Image


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='avatar.jpg', upload_to='profiles_avatar')
 
    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)

        img = Image.open(self.avatar.path)
        
        if img.height > 300 or img.width > 300:
            
            OUTPUT_SIZE = (300,300)

            img.thumbnail(OUTPUT_SIZE)

            img.save(self.avatar.path)