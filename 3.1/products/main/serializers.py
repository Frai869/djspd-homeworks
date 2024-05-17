from rest_framework import serializers

from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    # реализуйте все поля


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    comments = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'comments']
    # реализуйте поля title, description, price и reviews (список отзывов к товару)