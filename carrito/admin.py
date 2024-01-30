from django.contrib import admin
from .models import Categoria, Productos, Usuario, Boleta, detalle_boleta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Usuario)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)
