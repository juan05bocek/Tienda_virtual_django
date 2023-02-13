from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
# Create your views here.

@login_required(login_url='autenticacion/acceder')
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request,"productos/listado.html", {
        "productos": productos
    })
