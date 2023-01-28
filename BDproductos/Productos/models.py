from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre: models.CharField(max_length=300)
    destacado: models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/propductos', blank=True)
    detalle = models.TextField(max_length=1000, verbose_name='información del producto')
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-id']

