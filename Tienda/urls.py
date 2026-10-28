from django.urls import path

from . import views

app_name = 'Tienda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/<int:id>/', views.detalle, name='detalle'),
]
