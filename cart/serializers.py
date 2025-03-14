from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ('id',"owner","product","quantity",'total_price')

    def get_total_price(self,obj):
        return obj.total_price()