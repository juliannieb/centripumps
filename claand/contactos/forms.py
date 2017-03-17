from django import forms
from contactos.models import Pozo, Pertenece, Area, Atiende, Calificacion
from contactos.models import Nota, Recordatorio, Llamada
from contactos.models import NumeroTelefonico, TipoNumeroTelefonico
from empresas.models import Cliente
from principal.models import Vendedor

class PozoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=35, help_text='Nombre: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ubicacion = forms.CharField(max_length=35, help_text='Ubicacion: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.ModelChoiceField(queryset=Cliente.objects.all(), \
        help_text='Cliente: ', required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pozo
        fields = ('nombre', 'ubicacion', 'cliente',)

class LlamadaForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Pozo.objects.all(), help_text='Pozo: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Pozo
        fields = ('contacto', 'descripcion',)

class NotaForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Pozo.objects.all(), help_text='Pozo: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    clasificacion = forms.ChoiceField(help_text='Clasificación: ', choices=[(x, x) for x in range(1, 4)], \
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pozo
        fields = ('contacto', 'descripcion', 'clasificacion',)

class RecordatorioForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Pozo.objects.all(), help_text='Pozo: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    urgencia = forms.ChoiceField(help_text='Urgencia: ', choices=[(x, x) for x in range(1, 4)], \
        widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(help_text='Fecha y hora: ', \
        widget=forms.DateTimeInput(attrs={'class': 'form-control datepicker'}))

    class Meta:
        model = Recordatorio
        fields = ('contacto', 'descripcion', 'urgencia', 'fecha',)

class AtiendeForm(forms.ModelForm):
    vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.all(), help_text='Vendedor: ', \
        required=True, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Atiende
        fields = ('vendedor',)

class EditarPozoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=35, help_text='Nombre: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(max_length=35, help_text='Apellido: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.ModelChoiceField(queryset=Cliente.objects.all(), \
        help_text='Cliente: ', required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    area = forms.ModelChoiceField(queryset=Area.objects.all(), help_text='Area: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    calificacion = forms.ModelChoiceField(help_text='Calificación: ', \
        queryset=Calificacion.objects.all(), required=True, \
        widget=forms.Select(attrs={'class':'form-control'}))
    is_cliente = forms.BooleanField(help_text='Cliente: ', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-control'}))

    class Meta:
        model = Pozo
        fields = ('nombre', 'apellido', 'empresa', 'area', \
            'calificacion', 'is_cliente',)