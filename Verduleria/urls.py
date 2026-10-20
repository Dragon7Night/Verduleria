"""
URL configuration for Verduleria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Apps.gestionApp import views as app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.homeUni, name='homeUniversidad'),
    
    # --- RUTAS DE CATEGORÍA ---
    path('dataCategoria/', app1.categoriaData, name='categoriaDataName'),
    path('registroCategoria/', app1.registrarCategoria, name='categoriaRegisterN'),
    path('editarCategoria/<int:id>/', app1.editarCategoria, name='categoriaEditarN'),
    path('eliminarCategoria/<int:id>/', app1.eliminarCategoria, name='categoriaEliminarN'),
    
    # --- RUTAS DE PRODUCTO ---
    path('dataProducto/', app1.productoData, name='productoDataName'),
    path('registroProducto/', app1.registrarProducto, name='productoRegisterN'),
    path('editarProducto/<int:id>/', app1.editarProducto, name='productoEditarN'),
    path('eliminarProducto/<int:id>/', app1.eliminarProducto, name='productoEliminarN'),
]