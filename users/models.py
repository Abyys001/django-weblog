from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, blank=True)
    gmail = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
    




