from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categoria)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Post)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'autor', 'categoria', 'titulo', 'contenido', 'imagen', 'fecha_alta', 'fecha_actualizacion']