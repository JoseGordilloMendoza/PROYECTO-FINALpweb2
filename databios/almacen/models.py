from django.db import models

class product(models.Model):
    categoria = models.TextField()
    nombre= models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes/')
    stock= models.IntegerField()
    def __str__(self):
        return self.nombre
