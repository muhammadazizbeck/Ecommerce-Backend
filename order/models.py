from django.db import models
from django.contrib.auth import get_user_model
from market.models import Product

# Create your models here.

CustomUser = get_user_model()

class Order(models.Model):

    STATUS_CHOICES = [
        ('pending',"Pending"),
        ('completed','Completed'),
        ('canceled','Canceled'),
    ]
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return f"{self.id}-{self.owner.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity}*{self.product.name}- Order{self.order.id}"
    
    

