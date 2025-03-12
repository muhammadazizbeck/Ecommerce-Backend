from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True,unique=True)
    is_seller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_images',blank=True,null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

