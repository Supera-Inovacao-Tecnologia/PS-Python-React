from django.urls import path
from .views import OrderListCreate, OrderRetrieveUpdateDestroy

urlpatterns = [
path('', OrderListCreate.as_view(), name='order-list-create'),
path('<uuid>/', OrderRetrieveUpdateDestroy.as_view(), name='order-retrieve-update-destroy'),
]