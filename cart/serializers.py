from rest_framework import serializers
from .models import Cart, CartProducts
from products.models import Products
from django.forms.models import model_to_dict

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'createdAt', 'updatedAt',  'is_finished']

    def get_products(self, instance):
        cart = Cart.objects.get(user=instance.user)
        list_products = []
        products = CartProducts.objects.filter(cart=cart)
        for item in products:
            dict_product = model_to_dict(item)
            dict_product.pop('cart')
            list_products.append(dict_product)
        return list_products


class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ['cart', 'product', 'quantity']

    
    def get_extra_kwargs(self):
        cart = Cart.objects.get(user=self.context['request'].user)
        product = Products.objects.get(id=self.context['request'].data['product_id'])
        list_cart_product = CartProducts.objects.filter(cart=cart, product=product)
        
        if len(list_cart_product) > 0:
            CartProducts.objects.filter(product=product).delete()
            quatity_updated = list_cart_product[0].quantity+self.context['request'].data['quantity']
            self.context['request'].data['quantity'] = quatity_updated

        self.context['request'].data['cart'] = cart.id
        self.context['request'].data['product'] = product.id
        
        return super().get_extra_kwargs();

  