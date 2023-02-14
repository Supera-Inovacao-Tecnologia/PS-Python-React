from rest_framework import generics
from .models import Cart, CartProducts
from .serializers import CartSerializer, CartProductsSerializer
from products.models import Products
from rest_framework.views import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from users.permissions import UpdateAndDelete


class CartListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class CartCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UpdateAndDelete]
    queryset = CartProducts.objects.all()
    serializer_class = CartProductsSerializer


class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
