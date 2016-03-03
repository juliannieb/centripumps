from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify

class Cliente(models.Model):
    is_active = models.BooleanField(default=True)
    nombre_fiscal = models.CharField(max_length=50, default='')
    rfc = models.CharField(max_length=13, unique=True)
    slug = models.SlugField(unique=True, null=True)
    telefono1 = models.CharField(max_length=10, default='', null=True)
    telefono2 = models.CharField(max_length=10, default='', null=True)
    telefono3 = models.CharField(max_length=10, default='', null=True)

    direcciones = models.ManyToManyField('Direccion', through='ClienteTieneDireccion')
    correo1 = models.EmailField(null=True)
    correo2 = models.EmailField(null=True)
    correo3 = models.EmailField(null=True)
    nombre_contacto1 = models.CharField(max_length=50, null=True)
    nombre_contacto2 = models.CharField(max_length=50, null=True)
    nombre_contacto3 = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        """ Override de save para que el RFC siempre se guarde
        en mayusculas.
        """
        if not self.id and not self.slug:
            slug = slugify(self.nombre_fiscal)
            slug_exists = True
            counter = 1
            self.slug = slug
            while slug_exists:
                try:
                    slug_exits = Cliente.objects.get(slug=slug)
                    if slug_exits:
                        slug = self.slug + '_' + str(counter)
                        counter += 1
                except Cliente.DoesNotExist:
                    self.slug = slug
                    break
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_fiscal

class ClienteTieneDireccion(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey('Cliente')
    direccion = models.ForeignKey('Direccion')

    def save(self, *args, **kwargs):
        """ Override de save para que la fecha de creacion
        siempre sea la actual.
        """
        if not self.id:
            self.fecha = datetime.now()
        return super(ClienteTieneDireccion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cliente tiene direcciones'

class TipoRedSocial(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipo Redes Sociales'

class RedSocial(models.Model):
    is_active = models.BooleanField(default=True)
    link = models.URLField(null=True)
    empresa = models.ForeignKey(Cliente)
    tipo_red_social = models.ForeignKey(TipoRedSocial, null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Redes Sociales'

class Estado(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    is_active = models.BooleanField(default=True)
    direccion = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio)
    is_fiscal = models.BooleanField(default=False)

    def __str__(self):
        return self.direccion

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
