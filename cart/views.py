from django.shortcuts import render,get_object_or_404
from .models import Cart
from rest_framework.views import APIView
from .serializers import CartSerializer
from rest_framework import status,permissions
from rest_framework.response import Response

# Create your views here.

class CartListAPIView(APIView):
    def get(self,request):
        carts = Cart.objects.filter(owner=request.user)
        serializer = CartSerializer(carts,many=True)
        context = {
            'data':serializer.data,
            'status':"success",
        }
        return Response(context,status=status.HTTP_200_OK)
    
class CartAddAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        owner = request.user
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity',1))
        product = get_object_or_404(product,id=product_id)

        cart_item,created = Cart.objects.get_or_create(product=product,owner=owner)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

            return Response(CartSerializer(cart_item).data,status=status.HTTP_200_OK)
        return Response(CartSerializer(cart_item).data,status=status.HTTP_201_CREATED)

class CartDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request):
        Cart.objects.filter(owner=request.user).delete()
        context = {
            'status':'success',
            'message':'Savet tozalandi'
        }
        return Response(context,status=status.HTTP_204_NO_CONTENT)
    

class CartItemDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self,request,product_id):
        cart_item = get_object_or_404(Cart,owner=request.user,product_id=product_id)
        cart_item.delete()
        context = {
            'status':'success',
            'message':"Mahsulot savatdan o'chirildi"
        }
        return Response(context,status=status.HTTP_204_NO_CONTENT)

