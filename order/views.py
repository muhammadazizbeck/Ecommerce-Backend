from django.shortcuts import render,get_object_or_404
from .models import Order,OrderItem
from cart.models import Cart
from django.db import transaction
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions,status

# Create your views here.

class OrderListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        orders = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(orders,many=True)
        context = {
            'data':serializer.data,
            'status':'success',
        }
        return Response(context,status=status.HTTP_200_OK)
    
class OrderCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        cart_items = Cart.objects.filter(owner=request.user)

        if not cart_items:
            context = {
                'message':"Savat bo'sh mahsulotlarni tanlang"
            }
            return Response(context,status=status.HTTP_200_OK)
        
        with transaction.atomic():
            order = Order.objects.create(owner=request.user,total_price=0)
            total_price = 0

            for item in cart_items:
                order_item = OrderItem.objects.create(
                    order=order,
                    product = item.product,
                    quantity = item.quantity,
                    price = item.product.price*item.quantity
                )
                total_price += order_item.price

            order.total_price = total_price
            order.save()
            cart_items.delete()

        return Response(OrderSerializer(order).data,status=status.HTTP_200_OK)
    
class OrderDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,order_id):
        order = get_object_or_404(Order,id=order_id,owner=request.user)
        serializer = OrderSerializer(order)
        context = {
            'data':serializer.data,
            'status':'success',
        }
        return Response(context,status=status.HTTP_200_OK)
    
class OrderCancelAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request,order_id):
        order = get_object_or_404(Order,id=order_id,owner=request.user)
        if order.status != 'pending':
            context = {
                'status':'error',
                'error':"Buyurmalar bekor qilinishi mumkin"
            }
            return Response(context,status=status.HTTP_402_PAYMENT_REQUIRED)
        order.status = 'canceled'
        order.save()
        context = {
            'message':"Buyurtma bekor qilindi"
        }
        return Response(context,status=status.HTTP_200_OK)
    
        




