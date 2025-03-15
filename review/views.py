from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

# Create your views here.

class ReviewListAPIView(APIView):
    def get(self,request,product_id):
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews,many=True)
        context = {
            'data':serializer.data,
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    
class ReviewCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,product_id):
        data = request.data.copy()
        data['product']=product_id
        serializer = ReviewSerializer(data=data,context={'request':request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ReviewUpdateAPIView(APIView):
    permission_classes = [permissions.Authenticated] 

    def put(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id, owner=request.user)
        except Review.DoesNotExist:
            return Response({"error": "Sharh topilmadi yoki sizga tegishli emas"}, status=404)

        serializer = ReviewSerializer(review, data=request.data, partial=False)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id, owner=request.user)
        except Review.DoesNotExist:
            return Response({"error": "Sharh topilmadi yoki sizga tegishli emas"}, status=404)

        serializer = ReviewSerializer(review, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class ReviewDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id, owner=request.user)
        except Review.DoesNotExist:
            return Response({"error": "Sharh topilmadi yoki sizga tegishli emas"}, status=404)

        review.delete()
        return Response({"message": "Sharh o‘chirildi"}, status=204)


