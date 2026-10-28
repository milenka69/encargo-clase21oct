from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Producto


class TiendaUrlTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Libros",
            descripcion="Libros",
        )
        self.producto = Producto.objects.create(
            nombre="Libro de prueba",
            descripcion="Descripcion",
            precio=1000,
            stock=2,
            categoria=self.categoria,
        )

    def test_inicio_is_available_at_root_and_inicio(self):
        for url in (reverse("Tienda:inicio"), "/inicio/"):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, self.producto.nombre)

    def test_producto_detail_url_is_available(self):
        response = self.client.get(
            reverse("Tienda:detalle", args=[self.producto.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.producto.nombre)
