from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class product(models.Model):
    categoria = models.ManyToManyField(Categoria)
    nombre= models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes/')
    stock= models.IntegerField()
    def __str__(self):
        return self.nombre

