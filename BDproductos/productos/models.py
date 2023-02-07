from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length=300)
    destacado = models.BooleanField(default=False)

    def __srt__(self):
        return self.nombre

    class Meta:
        db_table ='categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    extracto = models.TextField(max_length=200, verbose_name='Extracto')
    detalle = models.TextField(max_length=1000, verbose_name='Información del producto')
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table ='productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
