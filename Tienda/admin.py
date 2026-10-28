from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, Categoria, Reserva

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
    list_display = ('nombre', 'descripcion', 'imagen')
    search_fields = ('nombre', 'descripcion')

    @admin.display(descripcion='Vista Previa')
    def imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height: 50px; border-radius: 5px;" />',
                obj.imagen.url
            )
        return '-'

@admin.register(Reserva)
class reservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha', 'personas', 'comentario', 'creada')
