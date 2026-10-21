from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(
        'Categoria', 
        on_delete=models.CASCADE, 
        related_name='productos'
    )

    class meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre