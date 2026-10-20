from django.contrib import admin

# Register your models here.

from Apps.gestionApp.models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nombre', 'precio', 'stock', 'unidad', 'categoria']

admin.site.register(Producto, ProductoAdmin)