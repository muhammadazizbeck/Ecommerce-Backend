from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    is_seller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_images',blank=True,null=True)

    def __str__(self):
        return self.username
    

