from django.urls import path
from .views import CartCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
path('<id>/product/', CartCreateView.as_view(), name='cart-list-create'),

path('<pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-delete'),
]