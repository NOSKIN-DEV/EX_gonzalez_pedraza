from django.urls import path
from . import views

from carrito.views import * 


urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('pagina_secundaria/', views.pagina_secundaria, name='pagina_secundaria'),
    path('pagina_galeria/', views.pagina_galeria, name='pagina_galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('modficar/<id>', views.modificar, name='modificar'),
    path('carrito/', views.carrito, name='carrito'),
    path('consultas/', views.consultas, name='consultas'),
    path('eliminarusuario/<id>', views.eliminarusuario, name='eliminarusuario'),
    path('registro/', views.registro, name='registro'),
    path('tienda/', views.tienda, name='tienda'),
    
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_producto, name="limpiar"),
    
]
