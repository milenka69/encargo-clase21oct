from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, Reserva

def inicio(request):
    productos = Producto.objects.select_related("categoria")

    cat = request.GET.get("Categoria")
    if cat:
        productos = productos.filter(categoria__id=cat)

    q = request.GET.get("q")
    if q:
        productos = productos.filter(nombre__icontains=q)

    return render(request, 'inicio.html', {"productos": productos, "categoria": Categoria.objects.all(),})

def detalle (request, id):
    producto = get_object_or_404 (Producto, id=id)
    return render(request, 'Tienda/detalle.html', {'producto': producto})
