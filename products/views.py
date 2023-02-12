from rest_framework import generics
from .serializers import ProductSerializer
from .models import ProductsModel

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer