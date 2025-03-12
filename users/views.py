from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerializer,PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status,permissions
from django.contrib.auth import update_session_auth_hash

# Create your views here.
class PasswordChangeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request):
        serializer = PasswordChangeSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            update_session_auth_hash(request,user)
            return Response({"message":"Parolingiz muvaffaqiyatli o'zgartirildi"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            context = {
                'user':serializer.data,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            }
            return Response(context,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error':"Refresh token talab qilinadi"},status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':"Tizimdan muvaffaqiyatli chiqdingiz"},status=status.HTTP_200_OK)
        except Exception:
            return Response({'error':'Yaroqsiz token'},status=status.HTTP_400_BAD_REQUEST)
    
    
                            

