from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos          
        fields = ['dv', 'nombre', 'descripcion', 'imagen']
        labels = {                
            'dv': 'Id',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'imagen':'Imagen'
        }
        widgets = {
            'dv' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id del producto..',
                    'id':'dv',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto..',
                    'id':'marca',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripición del producto..',
                    'id':'modelo',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }
