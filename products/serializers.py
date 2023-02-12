from rest_framework import serializers
from .models import ProductsModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('name', 'price', 'score', 'image')