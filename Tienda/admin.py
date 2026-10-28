from django.contrib import admin
from Tienda.models import Producto, Categoria, Reserva

@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formateado', 'stock', 'categoria__nombre')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria__nombre',)
    list_editable = ('stock',)

    def precio_formateado(self, obj):
        return f"${obj.precio: ,}".replace(',', '.')

@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Reserva)
class reservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha', 'personas', 'comentario', 'creada')
