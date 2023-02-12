from rest_framework import serializers
from .models import OrdersModel

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = ['user_id', 'id', 'total', 'createdAt']