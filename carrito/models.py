from django.db import models
import datetime
from django.http import HttpResponseForbidden

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Productos(models.Model):
    idProducto=models.CharField(primary_key=True, max_length=8, verbose_name='Id de Productos')
    nombreProducto=models.CharField(max_length=25, blank=True, verbose_name='Nombre')
    precio=models.FloatField(blank=True,  null=True,verbose_name='Precio')
    foto=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name='Imagen')
    descripcion=models.CharField(max_length=50, blank=True, verbose_name='Descripcion')
    categoria=models.ForeignKey(Categoria, default=1, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.idProducto


class Usuario(models.Model):
    nombre= models.CharField(primary_key= True, max_length=25,  verbose_name='Nombre')
    apellido = models.CharField(max_length=25, blank=True, verbose_name='Apellido') 
    correo = models.CharField(max_length=50, blank=True, verbose_name='Correo') 
    consulta = models.CharField(max_length=100, blank=True, verbose_name='Consulta') 
    
    def __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)
    
class detalle_boleta(models.Model):
    id_boleta=models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta=models.AutoField(primary_key=True)
    id_Producto=models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    subtotal=models.IntegerField()
    

    def __str__(self):
        return str(self.id_detalle_boleta)
    
