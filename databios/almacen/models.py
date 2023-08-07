from django.db import models
from django.contrib.auth.models import User


class DetectChanges(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.user_id:
            try:
                self.user = kwargs.pop('user')
            except KeyError:
                pass
        super(DetectChanges, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Categoria(DetectChanges):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Product(DetectChanges):

    categorias = models.ManyToManyField(Categoria)
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/')
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class itemCar(models.Model):
    producto = models.ForeignKey(Product,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

class ShoppingCar(models.Model):
    items=models.ForeignKey(itemCar,on_delete=models.CASCADE)





