from rest_framework import serializers
from .models import OrdersModel

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = ['user', 'id', 'total', 'createdAt']