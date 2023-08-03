from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from almacen.models import ShoppingCar
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    email = models.EmailField()
    telefono_celular = models.CharField(max_length=20, blank=True, null=True, validators=[MinLengthValidator(9)])
    carrito = models.OneToOneField(ShoppingCar,blank=True,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.username
