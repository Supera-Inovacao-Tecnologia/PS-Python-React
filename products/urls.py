from django.urls import path
from .views import ProductsListCreate, ProductsRetrieveUpdateDestroy

urlpatterns = [
path('', ProductsListCreate.as_view(), name='products_list_create'),
path('<pk>/', ProductsRetrieveUpdateDestroy.as_view(), name='products_retrieve_update_destroy'),
]
