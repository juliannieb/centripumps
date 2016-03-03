from django import forms
from empresas.models import Cliente, ClienteTieneDireccion, TipoRedSocial
from empresas.models import RedSocial, Estado, Municipio, Direccion
from contactos.models import NumeroTelefonico, TipoNumeroTelefonico

class ClienteForm(forms.ModelForm):
	nombre_fiscal = forms.CharField(max_length=30, help_text='Nombre Fiscal: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	rfc = forms.RegexField(max_length=13, help_text='RFC: ', regex=r'[a-zA-Z0-9]{13}', \
		required=True, error_message ="Debe contener 13 letras y números", \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	nombre_contacto1 = forms.CharField(max_length=20, help_text='Nombre contacto 1: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombre_contacto2 = forms.CharField(max_length=20, help_text='Nombre contacto 2: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombre_contacto3 = forms.CharField(max_length=20, help_text='Nombre contacto 3: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	telefono1 = forms.IntegerField(help_text='Teléfono 1: ', required=False, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))
	telefono2 = forms.IntegerField(help_text='Teléfono 2: ', required=False, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))
	telefono3 = forms.IntegerField(help_text='Teléfono 3: ', required=False, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))

	correo1 = forms.CharField(max_length=20, help_text='Correo contacto 1: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	correo2 = forms.CharField(max_length=20, help_text='Correo contacto 2: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	correo3 = forms.CharField(max_length=20, help_text='Correo contacto 3: ', required=False, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	

	class Meta:
		model = Cliente
		fields = ('nombre_fiscal', 'rfc', 'nombre_contacto1', 'nombre_contacto2', 'nombre_contacto3', 'telefono1', 'telefono2', 'telefono3', 'correo1', 'correo2', \
			'correo3', )

	def clean(self):
		cleaned_data = self.cleaned_data


class DireccionForm(forms.ModelForm):
	direccion = forms.CharField(max_length=100, help_text='Dirección: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), help_text='Estado: ', \
		required=False, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'id_estado'}))
	municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), help_text='Municipio: ', \
		required=True, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'id_municipio'}))

	class Meta:
		model = Direccion
		fields = ('estado', 'municipio', 'direccion',)

class NumeroTelefonicoForm(forms.ModelForm):
	numero = forms.IntegerField(help_text='Número: ', required=True, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))
	tipo_numero = forms.ModelChoiceField(queryset=TipoNumeroTelefonico.objects.all(), \
		help_text='Tipo: ', required=True, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = NumeroTelefonico
		fields = ('numero', 'tipo_numero',)

class RedSocialForm(forms.ModelForm):
	link = forms.URLField(help_text='Link: ', required=True, \
		widget=forms.URLInput(attrs={'class': 'form-control'}))
	tipo_red_social = forms.ModelChoiceField(queryset=TipoRedSocial.objects.all(), \
		help_text='Tipo: ', required=True, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = RedSocial
		fields = ('link', 'tipo_red_social',)