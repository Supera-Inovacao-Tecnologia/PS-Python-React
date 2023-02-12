from rest_framework import serializers
from .models import User

from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'cellphone', 'is_active']
                

    def create(self, validate_data: dict):
        create_user = User.objects.create_user(**validate_data)
        return create_user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'cellphone', 'password', 'is_active']


class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cellphone', 'is_active']


class UserDeactiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
