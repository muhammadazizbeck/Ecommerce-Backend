from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class CategoryListAPIView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        context = {
            'data':serializer.data,
            'status':"success",
        }
        return Response(context,status=status.HTTP_200_OK)
    
class ProductListAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        context = {
            'data':serializer.data,
            'status':"success"
        }
        return Response(context,status=status.HTTP_200_OK)
    
class ProductCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer = ProductSerializer(data=request.data,files=request.FILES)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            context = {
                'data':serializer.data,
                'status':"success",
                "message":"Mahsulot muvaffaqiyatli qo'shildi"
            }
            return Response(context,status=status.HTTP_201_CREATED)
        context = {
            'errors':serializer.errors,
            "status":"error",
            'message':"Ma'lumotni tekshiring!"
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        try:
            product = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(product)
            context = {
                'data':serializer.data,
                'status':"success",
                "message":"Mahsulot topildi"
            }
            return Response(context,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            context = {
                'status':'error',
                "message":"Mahsulot topilmadi"
            }
            return Response(context,status=status.HTTP_404_NOT_FOUND)
        
class ProductUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk,user):
        try:
            product = get_object_or_404(Product,pk=pk)
            if product.owner != user:
                return None
            return product
        except Product.DoesNotExist:
            return None
        
    
    def put(self,request,pk):
        product = self.get_object(pk,request.user)
        if not product:
            context = {
                'status':'error',
                "message":"Mahsulot topilmadi yoki sizga tegishli emas",
            }
            return Response(context,status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(data=request.data,files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data,
                'status':"success",
                'message':"Mahsulot muvaffaqiyatli taxrirlandi",
            }
            return Response(context,status=status.HTTP_201_CREATED)
        context = {
            'errors':serializer.errors,
            'status':'success',
            'message':"Ma'lumotni tekshiring"
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    

class ProductDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk,user):
        try:
            product = get_object_or_404(Product,pk=pk)
            if product.owner != user:
                return None
            return product
        except Product.DoesNotExist:
            return None
        
    def delete(self,request,pk):
        product = self.get_object(pk,request.user)
        if not product:
            context = {
                'status':'error',
                'message':"Mahsulot topilmadi yoki sizga tegishli emas"
            }
            return Response(context,status=status.HTTP_403_FORBIDDEN)
        product.delete()
        context = {
            'status':'success',
            'message':"Mahsulot muvaffaqiyatli o'chirildi"
        }
        return Response(context,status=status.HTTP_204_NO_CONTENT)
    


            


