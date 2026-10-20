from django.shortcuts import render
from Apps.gestionApp.models import Categoria, Producto
from Apps.gestionApp.forms import RegistroCategoriaModelForm, RegistroProductoModelForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def homeUni(request):
    data = {'imgLogo':'img/logo.jpg'}
    return render(request, 'gestionApp/index.html', data)


# ----------[view para la CATEGORÍA]-------------------------------------------------

def categoriaData(request):
    categoriaObject = Categoria.objects.all()
    data = {
        'categoriaKey': categoriaObject,
        'mainTitle': 'Registros de categorías',
        'titulo': 'Categorías registradas',
        'colorBg': 'text-bg-success'
    }
    return render(request, 'gestionApp/dataCategoria.html', data)


def registrarCategoria(request):
    form = RegistroCategoriaModelForm()
    if request.method == 'POST':
        form = RegistroCategoriaModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriaDataName'))
        
    data = {
        'formKey': form,
        'mainTitle': 'Registro de categorías',
        'txtForm': 'Formulario de registro categorías',
        'txtBtn': 'Registrar categoría',
        'colorBg': 'text-bg-warning'
    }
    return render(request, 'gestionApp/registroUsuarios.html', data)


def editarCategoria(request, id):
    categoriaObjects = Categoria.objects.get(id=id)
    form = RegistroCategoriaModelForm(instance=categoriaObjects) 

    if request.method == 'POST':
        form = RegistroCategoriaModelForm(request.POST, instance=categoriaObjects) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriaDataName'))
    
    data = {
        'formKey': form,
        'txtForm': 'Modificar datos de la categoría',
        'txtBtn': 'Confirmar cambios',
        'colorBg': 'text-bg-info'
    }
    return render(request, 'gestionApp/registroUsuarios.html', data)


def eliminarCategoria(request, id):
    categoriaObjects = Categoria.objects.get(id=id)
    categoriaObjects.delete()
    return HttpResponseRedirect(reverse('categoriaDataName'))



# ----------[view para el PRODUCTO]-------------------------------------------------

def productoData(request):
    productoObject = Producto.objects.all()
    data = {
        'productoKey': productoObject,
        'mainTitle': 'Registros de productos',
        'titulo': 'Productos registrados',
        'colorBg': 'text-bg-danger'
    }
    return render(request, 'gestionApp/dataProducto.html', data)


def registrarProducto(request):
    form = RegistroProductoModelForm()
    if request.method == 'POST':
        form = RegistroProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productoDataName'))
        
    data = {
        'formKey': form,
        'mainTitle': 'Registro de productos',
        'txtForm': 'Formulario de registro productos',
        'txtBtn': 'Registrar producto',
        'colorBg': 'text-bg-warning'
    }
    return render(request, 'gestionApp/registroUsuarios.html', data)


def editarProducto(request, id):
    productoObjects = Producto.objects.get(id=id)
    form = RegistroProductoModelForm(instance=productoObjects) 

    if request.method == 'POST':
        form = RegistroProductoModelForm(request.POST, instance=productoObjects) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productoDataName'))

    data = {
        'formKey': form,
        'txtForm': 'Modificar datos del producto',
        'txtBtn': 'Confirmar cambios',
        'colorBg': 'text-bg-info'
    }
    return render(request, 'gestionApp/registroUsuarios.html', data)


def eliminarProducto(request, id):
    productoObjects = Producto.objects.get(id=id)
    productoObjects.delete()
    return HttpResponseRedirect(reverse('productoDataName'))