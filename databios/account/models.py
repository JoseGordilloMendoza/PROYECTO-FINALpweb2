from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from almacen.models import ShoppingCar
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    email = models.EmailField()
    telefono_celular = models.CharField(max_length=20, blank=True, null=True, validators=[MinLengthValidator(9)])
    carrito = models.OneToOneField(ShoppingCar, null=True, on_delete=models.CASCADE)
    # Reemplaza 'nombre_de_tu_app' con el nombre de tu aplicación donde está definido el modelo ShoppingCar
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_users'  # Aquí defines el related_name para el modelo Group
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_users_permissions'  # Aquí defines el related_name para el modelo Permission
    )
    def __str__(self):
       return self.username
