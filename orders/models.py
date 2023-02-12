from django.db import models
import uuid
from products.models import ProductsModel
from users.models import User


class OrdersModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)


class OrderProductsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)