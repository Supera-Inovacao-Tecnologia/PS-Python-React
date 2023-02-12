from rest_framework import generics
from .serializers import OrdersSerializer
from .models import OrdersModel

class OrderListCreate(generics.ListCreateAPIView):
    queryset = OrdersModel.objects.all()
    serializer_class = OrdersSerializer

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdersModel.objects.all()
    serializer_class = OrdersSerializer