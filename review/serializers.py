from .models import Review
from rest_framework import serializers
from rest_framework.validators import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ('id','owner','product','rating','comment','created_at')

    def validate(self, data):
        request = self.context['request']
        owner = request.user
        product = data['product']

        if not owner.orders.filter(orderitem__product=product).exists():
            raise ValidationError('Siz hali mahsulot sotib olmagansiz')
        return data
        