from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import os

# Create your views here.
def index(request):
     return render(request, 'index.html')

def vision(request):
     return render(request, 'vision.html')

def tienda(request):
     productos = Productos.objects.all()
     datos={
        'productos':productos
    }
     return render(request,'tienda.html',datos)

def adopcion(request):
     return render(request, 'adopcion.html')

def registrar(request):
     data={
        'form':RegistroUserForm()
     }
     if request.method=="POST":
          formulario = RegistroUserForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
               login(request,user)
               return redirect ('index')
          data["form"] = formulario
     return render(request, 'registration/registrar.html',data)

@login_required
def crear(request):
    if request.method=="POST":
        productosform = ProductosForm(request.POST, request.FILES)
        if productosform.is_valid():
            productosform.save()     #similar al insert
            return redirect('tienda')
    else:
        productosform=ProductosForm()
    return render(request, 'crear.html', {'productosform':productosform})

@login_required
def modificar(request, id):
     producto = Productos.objects.get(dv=id)
     if request.method=='POST':
          if len(request.FILES)!=0:
               if len(producto.imagen)>0:
                    os.remove(producto.imagen.path)
               producto.imagen=request.FILES['imagen']
          producto.nombre=request.POST.get('nombre')
          producto.descripcion=request.POST.get('descripcion')
          producto.save()
          return redirect('tienda')
     datos = {
          'form': ProductosForm(request.POST,request.FILES,instance=producto)
     }
     return render(request, 'modificar.html', datos)

@login_required
def eliminar(request, id):
    productoEliminado = Productos.objects.get(dv=id) #obtenemos un objeto por su id
    productoEliminado.delete()
    return redirect ('tienda')