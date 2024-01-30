from django.shortcuts import render, redirect
from .models import Categoria, Productos, Usuario, Boleta, detalle_boleta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ProductosForm, ContactoForm, RegistroUserForm
from carrito.compra import Carrito

# Create your views here.



def inicio(request):
    return render(request, 'inicio.html')

def pagina_secundaria(request):
    return render(request, 'pagina_secundaria.html')



def pagina_galeria(request):
    return render(request, 'pagina_galeria.html')

def contacto(request):
    if request.method=='POST':
        #creamos un objeto de tipo VehiculoForm
        contacto_form = ContactoForm(request.POST, request.FILES)
        if contacto_form.is_valid():     
            #almacena el objeto en el backend
            contacto_form.save()        #similar al insert de una BDR
            
    else:
        contacto_form=ContactoForm()
    return render(request, 'contacto.html', {'contacto_form': contacto_form})

def catalogo(request):
    return render(request, 'catalogo.html')



def carrito(request):
    productos = Productos.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'carrito.html', datos)

def tienda(request):
    productos= Productos.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'tienda.html', datos)


@login_required
def consultas(request):
    usuario = Usuario.objects.all()
    datos={
        'usuario': usuario
    }
    return render (request, 'consultas.html', datos)
    
@login_required
def eliminarusuario(request, id):
    usuario = Usuario.objects.get(nombre=id) #similar a select * from where patente=id
    usuario.delete()           #eliminación fisica del backend
    return redirect ('consultas')

@login_required
def mostrar(request):
    productos = Productos.objects.all()
    datos={
        'productos':productos
    }
    return render(request, 'mostrar.html', datos)

@login_required
def crear(request):
    if request.method=='POST':
        productos_form = ProductosForm(request.POST, request.FILES)
        if productos_form.is_valid():
            productos_form.save()
            return redirect('crear')
    else:
        productos_form = ProductosForm()
    return render(request, 'crear.html', {'productos_form': productos_form})


@login_required
def eliminar(request, id):
    producto = Productos.objects.get(idProducto=id)
    producto.delete()
    return redirect('mostrar')

@login_required
def modificar(request, id):
    producto = Productos.objects.get(idProducto=id)
    datos={
        'formMod': ProductosForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductosForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar')
    return render(request, 'modificar.html', datos)

def registro(request):
    data={
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('inicio')
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)

def agregar_producto(request, id):
    carrito_compra= Carrito(request)
    productos = Productos.objects.get(idProducto=id)
    carrito_compra.agregar(productos=productos)
    return redirect ('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    productos = Productos.objects.get(idProducto=id)
    carrito_compra.eliminar(productos=productos)
    return redirect ('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    productos = Productos.objects.get(idProducto=id)
    carrito_compra.restar(productos=productos)
    return redirect ('tienda')

def limpiar_producto(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect ('tienda')

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + float(value['precio']) * float(value['cantidad'])
    boleta= Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Productos.objects.get(idProducto = value['id'])
        cant = value["cantidad"]
        subtotal = cant * float(value["precio"])
        
        detalle = detalle_boleta(id_boleta = boleta, id_Producto = producto, cantidad =cant, subtotal =subtotal)
        detalle.save()
        productos.append(detalle)
    datos={
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session["boleta"] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request ,'detallecarrito.html', datos)
