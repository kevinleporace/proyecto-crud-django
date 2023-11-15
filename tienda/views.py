from django.shortcuts import render,redirect
from .models import Producto
from django.contrib import messages

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
    messages.success(request,'producto enviado')
    return redirect('consultar')

def eliminar(request,id):
    producto=Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request,'producto eliminado')
    return redirect('consultar')

def detalle(request,id):
    producto=Producto.objects.get(pk=id)
   
    return render(request,'productoEditar.html',{'producto' :producto})

def editar(request):
    nombre=request.POST["nombre"]
    precio=request.POST["precio"]
    descripcion=request.POST["descripcion"]
    id=request.POST["id"]
    Producto.objects.filter(pk=id).update(id=id,nombre=nombre,precio=precio,descripcion=descripcion)
    messages.success(request,'producto actualizado')
    return redirect('consultar')

