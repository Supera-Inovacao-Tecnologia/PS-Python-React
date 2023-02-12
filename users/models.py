import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cellphone = models.CharField(max_length=12, null=False, blank=False, unique=True)
    ...        
    
    