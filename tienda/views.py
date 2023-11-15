from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def home(request):
    return render(request,'principal.html')

def consultar(request):
    productos=Producto.objects.all()
    return render(request,'productos.html',{
        'productos':productos
    })

def guardar(request):
    nombre=request.POST["nombre"]
    precio=request.POST["precio"]
    descripcion=request.POST["descripcion"]
    #el de la izquierda es el nombre en el modelo ,el de la derecha es el 
    #del formulario
    p=Producto(nombre=nombre,precio=precio,descripcion=descripcion)
    p.save()
    return redirect('consultar')