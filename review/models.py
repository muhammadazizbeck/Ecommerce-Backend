from django.db import models
from django.contrib.auth import get_user_model
from market.models import Product

# Create your models here.

CustomUser = get_user_model()

class Review(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(choices=[(i,str(i)) for i in range(1,6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} commented on {self.product}"
    
    class Meta:
        unique_together = ('owner','product')