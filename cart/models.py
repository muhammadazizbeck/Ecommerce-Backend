from django.db import models
from django.contrib.auth import get_user_model
from market.models import Product

# Create your models here.

CustomUser = get_user_model()

class Cart(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price*self.quantity
    
    def __str__(self):
        return f"{self.owner.username}-{self.product.name}"
    
    

    
