from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

CustomUser = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
