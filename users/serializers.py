from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

CustomUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model = CustomUser
        fields = ['username','email','password','address','phone','is_seller','image']

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True,min_length=8)

    def validate(self,data):
        identifier = data.get('identifier')
        password = data.get('password')

        user = CustomUser.objects.filter(email=identifier).first()

        if not user:
            user = CustomUser.objects.filter(username=identifier).first()

        if not user or not user.check_password(password):
            raise ValidationError("Username yoki Email yoki Parol xato!")
        
        if not user.is_active:
            raise ValidationError('Acconunt Blocklangan')
        
        tokens = RefreshToken.for_user(user)
        return {
            "user": {
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'address':user.address,
                'phone':user.phone,
                'is_seller':user.is_seller,
                'image':user.image.url if user.image else None
            },
            'refresh':str(tokens),
            'access':str(tokens.access_token),
        }

        