from rest_framework import serializers
from .models import User
from cart.models import Cart, CartProducts
from django.forms.models import model_to_dict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'email', 'cellphone', 'is_active']

    def create(self, validate_data: dict):
        create_user = User.objects.create_user(**validate_data)
        Cart.objects.create(user=create_user)
        return create_user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'cellphone', 'password', 'is_active']


class UserRetriveSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'cellphone', 'is_active', 'cart']

    def get_cart(self, instance):
        cart = Cart.objects.get(user=instance)
        new_cart = model_to_dict(cart)
        new_cart.pop('user')
        new_cart['products'] = []
        products = CartProducts.objects.filter(cart=cart)
        for item in products:
            new_cart['products'].append(model_to_dict(item))

        return new_cart

    # def to_representation(self, instance):
    #     cart = Cart.objects.get(user=instance)
    #     new_cart = model_to_dict(cart)
    #     new_cart['products'] = []
    #     products = CartProducts.objects.filter(cart=cart)
    #     for item in products:
    #         new_cart['products'].append(model_to_dict(item))
    #     user_dict = model_to_dict(instance)
    #     user_dict['cart'] = new_cart

    #     return {'username': 'User1', 'is_active': True,
    #              'email': 'user1@mail.com', 'cellphone': '021992248141',  'cart': {'is_finished': False, 'products': new_cart['products'] }}


class UserDeactiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
