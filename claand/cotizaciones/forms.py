from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from cotizaciones.models import *
from contactos.models import Pozo

class CotizacionForm(forms.ModelForm):
	contacto = forms.ModelChoiceField(queryset=Pozo.objects.all(), help_text='Pozo: ', \
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	monto = forms.FloatField(help_text='Monto: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
	descripcion = forms.CharField(help_text='Descripción: ', \
		required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

	class Meta:
		model = Cotizacion
		fields = ('contacto', 'monto', 'descripcion',)

class VentaForm(forms.ModelForm):
	monto_total = forms.FloatField(help_text='Monto total: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Venta
		fields = ('monto_total',)

class PagoForm(forms.ModelForm):
	monto = forms.FloatField(help_text='Monto total: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Pago
		fields = ('monto',)

class ProveedorForm(forms.ModelForm):
	nombre = forms.CharField(help_text='Nombre: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	telefono = forms.IntegerField(help_text='Número: ', required=True, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Proveedor
		fields = ('nombre', 'telefono',)

class ProductoForm(forms.ModelForm):
	nombre = forms.CharField(help_text='Nombre: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	lugar = forms.CharField(help_text='Lugar: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	cantidad = forms.IntegerField(help_text='Cantidad: ', required=True, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Producto
		fields = ('nombre', 'lugar', 'cantidad',)

class ServicioForm(forms.ModelForm):
	nombre = forms.CharField(help_text='Nombre: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Servicio
		fields = ('nombre',)

class VendeForm(forms.ModelForm):
	proveedor = forms.ModelChoiceField(help_text='Proveedor: ',queryset=Proveedor.objects.all().order_by('nombre'),
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	producto = forms.ModelChoiceField(help_text='Producto: ',queryset=Producto.objects.all().order_by('nombre'),
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	precio = forms.FloatField(help_text='Precio: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Vende
		fields = ('proveedor', 'producto', 'precio')

class BrindaForm(forms.ModelForm):
	proveedor = forms.ModelChoiceField(help_text='Proveedor: ', queryset=Proveedor.objects.all().order_by('nombre'),
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	servicio = forms.ModelChoiceField(help_text='Servicio: ',queryset=Servicio.objects.all().order_by('nombre'),
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	precio = forms.FloatField(help_text='Precio: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Brinda
		fields = ('proveedor', 'servicio', 'precio')