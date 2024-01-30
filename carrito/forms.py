from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Categoria, Productos, Usuario
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email', 'password1', 'password2']


class ProductosForm(forms.ModelForm):
    class Meta:
        model= Productos
        fields=['idProducto','nombreProducto','precio','foto','descripcion','categoria']
        labels={
            'idProducto': 'Id',
            'nombreProducto':'Nombre',
            'precio':'Precio',
            'foto':'Imagen',
            'descripcion':'Descripcion',
            'categoria':'Categoria',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Identificador',
                    'id': 'idProducto'
                }
            ),
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id':'nombreProducto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio del producto',
                    'id':'precio'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'foto'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese descripcion',
                    'id': 'descripcion'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class':'form-control',
                    'id': 'categoria'
                }
            )
        }
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'consulta']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'consulta': 'Consulta',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'minlength':'minimo 3 caracteres',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'minlength':'minimo 3 caracteres',
                    'id': 'apellido'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'correo'
                }
            ),
            'consulta': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su consulta',
                    'id': 'consulta'
                }
            )
        }
