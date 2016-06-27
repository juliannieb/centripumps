from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator

from contactos.models import Pozo

""" Los objetos tipo concepto, componen las cotizaciones y ventas,
    se dividen en servicios y productos """
class Producto(models.Model):
    is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=30)
    lugar = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nombre)

class Servicio(models.Model):
    is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Servicio, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    is_active = models.BooleanField(default=True)
    monto = models.FloatField(default=0, validators=[MinValueValidator(0)])
    descripcion = models.TextField()
    is_pendiente = models.BooleanField(default=True)
    contacto = models.ForeignKey(Pozo)
    productos = models.ManyToManyField(Producto, through='CotizacionUtilizaProducto')
    servicios = models.ManyToManyField(Servicio, through='CotizacionUtilizaServicio')
    fecha_creacion = models.DateField(editable=True)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Cotizacion, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.contacto) + ": " + self.descripcion + ": $" + str(self.monto)

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'

class Venta(models.Model):
    is_active = models.BooleanField(default=True)
    monto_total = models.FloatField(default=0, validators=[MinValueValidator(0)])
    monto_acumulado = models.FloatField(default=0)
    is_completada = models.BooleanField(default=False)
    cotizacion = models.OneToOneField(Cotizacion)
    fecha_creacion = models.DateField(editable=True)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.cotizacion.contacto) + ": " + self.cotizacion.descripcion + ": $" + \
        str(self.monto_total)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class Pago(models.Model):
    is_active = models.BooleanField(default=True)
    venta = models.ForeignKey(Venta)
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()
    monto = models.FloatField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        """ Override de save para que sólo haya una fecha de creación,
        y si dicha tupla se modifica, se guarde la fecha de modificación.
        """
        if not self.id:
            self.fecha_creacion = datetime.today()
        self.fecha_modificacion = datetime.today()
        return super(Pago, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ": " + self.venta.cotizacion.descripcion + ": $" + \
        str(self.monto)

class Proveedor(models.Model):
    is_active = models.BooleanField(default=True)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    productos = models.ManyToManyField(Producto, through='Vende')
    servicios = models.ManyToManyField(Servicio, through='Brinda')
    fecha_creacion = models.DateField(editable=False)
    fecha_modificacion = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_creacion = datetime.now()
        self.fecha_modificacion = datetime.now()
        return super(Proveedor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nombre)

class Vende(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.FloatField(default=0.0, validators=[MinValueValidator(0)])
    fecha_creacion = models.DateField(editable=False, null=True)
    fecha_modificacion = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_creacion = datetime.now()
        self.fecha_modificacion = datetime.now()
        return super(Vende, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.proveedor) + " - " + str(self.producto) + " - $" + str(self.precio)


class Brinda(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.FloatField(default=0.0, validators=[MinValueValidator(0)])
    fecha_creacion = models.DateField(editable=False, null=True)
    fecha_modificacion = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_creacion = datetime.now()
        self.fecha_modificacion = datetime.now()
        return super(Brinda, self).save(*args, **kwargs)

class CotizacionUtilizaProducto(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

class CotizacionUtilizaServicio(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
