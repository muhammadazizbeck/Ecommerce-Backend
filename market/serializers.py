from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),write_only=True,source='category'
    )
    class Meta:
        model = Product
        fields = ("id","name","description","price","stock","category","category_id","created_at","image","owner")

