from django.db import models
import uuid
from products.models import Products
from users.models import User


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    delivery = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.subtotal + self.delivery
        super().save(*args, **kwargs)
        
        

class OrderProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
