from django import forms
from Apps.gestionApp.models import Categoria, Producto
from django.core import validators

# ---↓↓↓--[FORMULARIO DE CATEGORÍA]--↓↓↓------------------------------------------------

# EDITAR una categoría (Form estándar)
class RegistroCategoriaForm(forms.Form):
    
    # Definición de campos + validaciones
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(2),
        validators.MaxLengthValidator(50)
    ])

    # Estilo Bootstrap 5 (BS5)
    nombre.widget.attrs['class'] = 'form-control'

    # Etiqueta personalizada
    nombre.label = 'Nombre de la Categoría'


# REGISTRAR una categoría (ModelForm)
class RegistroCategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    # Definición de campos + validaciones
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(2),
        validators.MaxLengthValidator(50)
    ])

    # Estilo Bootstrap 5 (BS5)
    nombre.widget.attrs['class'] = 'form-control'

    # Etiqueta personalizada
    nombre.label = 'Nombre de la Categoría'


# ---↓↓↓--[FORMULARIO DE PRODUCTO]--↓↓↓------------------------------------------------

# EDITAR un producto (Form estándar)
class RegistroProductoForm(forms.Form):

    # Definición de campos + validaciones
    codigo = forms.IntegerField(validators=[
        validators.MinValueValidator(1)
    ])
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(50)
    ])
    precio = forms.DecimalField(validators=[
        validators.MinValueValidator(0)
    ], max_digits=10, decimal_places=2)
    stock = forms.IntegerField(validators=[
        validators.MinValueValidator(0)
    ])
    unidad = forms.IntegerField(validators=[
        validators.MinValueValidator(0)
    ])
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    # Estilo Bootstrap 5 (BS5)
    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'
    unidad.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

    # Etiquetas personalizadas
    codigo.label = 'Código'
    nombre.label = 'Nombre'
    precio.label = 'Precio'
    stock.label = 'Stock'
    unidad.label = 'Unidad'
    categoria.label = 'Categoría'


# REGISTRAR un producto (ModelForm)
class RegistroProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    # Definición de campos + validaciones
    codigo = forms.IntegerField(validators=[
        validators.MinValueValidator(1)
    ])
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(50)
    ])
    precio = forms.DecimalField(validators=[
        validators.MinValueValidator(0)
    ], max_digits=10, decimal_places=2)
    stock = forms.IntegerField(validators=[
        validators.MinValueValidator(0)
    ])
    unidad = forms.IntegerField(validators=[
        validators.MinValueValidator(0)
    ])
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    # Estilo Bootstrap 5 (BS5)
    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'
    unidad.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

    # Etiquetas personalizadas
    codigo.label = 'Código'
    nombre.label = 'Nombre'
    precio.label = 'Precio'
    stock.label = 'Stock'
    unidad.label = 'Unidad'
    categoria.label = 'Categoría'

    