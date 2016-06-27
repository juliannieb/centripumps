from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date
from django.forms.util import ErrorList

from cotizaciones.models import Cotizacion, Venta, Pago
from principal.models import Vendedor
from contactos.models import Pertenece

from cotizaciones.forms import *

def no_es_vendedor(user):
    """ Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

def obtener_contactos_list(vendedor):
    todos_los_contactos = Pozo.objects.all()
    contactos_list = []
    for contacto in todos_los_contactos:
        atiende_set = contacto.atiende_set.all()
        if atiende_set:
            ultimo_atiende = atiende_set[len(atiende_set) - 1]
            if ultimo_atiende.vendedor == vendedor:
                if contacto.is_active:
                    contactos_list.append(contacto)
    return contactos_list

def obtener_cotizaciones_list(contactos_list):
    todas_las_cotizaciones = Cotizacion.objects.all()
    cotizaciones_list = []
    for cotizacion in todas_las_cotizaciones:
        for contacto in contactos_list:
            atiende_set = contacto.atiende_set.all()
            if atiende_set:
                ultimo_atiende = atiende_set[len(atiende_set) - 1]
                if cotizacion.contacto == contacto and cotizacion.fecha_creacion >= ultimo_atiende.fecha:
                    if cotizacion.is_active:
                        cotizaciones_list.append(cotizacion)
    return cotizaciones_list

def obtener_ventas_list(cotizaciones_list):
    todas_las_ventas = Venta.objects.all()
    ventas_list = []
    for venta in todas_las_ventas:
        for cotizacion in cotizaciones_list:
            if venta.cotizacion == cotizacion:
                if venta.is_active:
                    ventas_list.append(venta)
    return ventas_list

def obtener_contactos_ids(contactos_list):
    contactos_ids = []
    for contacto in contactos_list:
        contactos_ids.append(contacto.id)
    return contactos_ids

@login_required
def consultar_cotizaciones(request):
    """ Vista para mostrar todas las cotizaciones de un usuario.
    """
    current_user = request.user
    if no_es_vendedor(current_user):
        cotizaciones_list = Cotizacion.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Pozo.objects.all()
        contactos_list = obtener_contactos_list(current_vendedor)
        cotizaciones_list = obtener_cotizaciones_list(contactos_list)

    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['cotizaciones_list'] = cotizaciones_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'cotizaciones/cotizaciones.html', context)

@login_required
def cotizacion(request, id_cotizacion):
    """ Vista para mostrar el detalle de una cotizacion.
    """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['cotizacion'] = cotizacion
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['no_es_vendedor'] = es_vendedor
    return render(request, "cotizaciones/cotizacion.html", context)

@login_required
def consultar_ventas(request):
    """ Vista para mostrar todas las ventas asociadas a un usuario.
    En el caso del director, se muestran todas las ventas globales.
    """
    current_user = request.user
    if no_es_vendedor(current_user):
        ventas_list = Venta.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Pozo.objects.all()
        contactos_list = obtener_contactos_list(current_vendedor)
        cotizaciones_list = obtener_cotizaciones_list(contactos_list)
        ventas_list = obtener_ventas_list(cotizaciones_list)
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['ventas_list'] = ventas_list
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'cotizaciones/ventas.html', context)

@login_required
def venta(request, id_venta):
    """ Vista para mostrar el detalle de una venta en particular.
    """
    venta = Venta.objects.get(id=id_venta)
    id_cotizacion = venta.cotizacion.id
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)
    pagos_list = Pago.objects.filter(venta=venta)
    context = {}
    context['venta'] = venta
    context['cotizacion'] = cotizacion
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['no_es_vendedor'] = es_vendedor
    context['pagos_list'] = pagos_list
    return render(request, 'cotizaciones/venta.html', context)


@login_required
def registrar(request):
    """ Vista para registrar una cotizacion.
    """
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = obtener_contactos_list(current_vendedor)
    contactos_list = obtener_contactos_ids(contactos_list)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = Pozo.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}
        if formCotizacion.is_valid():
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            Cotizacion(contacto=contacto, monto=monto, descripcion=descripcion).save()
            return render(request, 'principal/exito.html')
    else:
        formCotizacion = CotizacionForm()
        formCotizacion.fields["contacto"].queryset = Pozo.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_cotizacion.html', forms)

@login_required
def registrar_venta(request, id_cotizacion):
    """ Vista para registrar una venta.
    En esta misma se cambia el status de una cotizacion a no pendiente.
    """
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    current_user = request.user
    if request.method == 'POST':
        formVenta = VentaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'cotizacion' : cotizacion, 'no_es_vendedor':es_vendedor}
        if formVenta.is_valid():
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            cotizacion.is_pendiente = False
            cotizacion.save()
            contacto = cotizacion.contacto
            if contacto.is_cliente == False:
                contacto.is_cliente = True
                contacto.save()
            Venta(monto_total=monto_total, cotizacion=cotizacion).save()
            return render(request, 'principal/exito.html')
    else:
        formVenta = VentaForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'cotizacion' : cotizacion}
    return render(request, 'cotizaciones/registrar_venta.html', forms)


@login_required
def registrar_pago(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formPago = PagoForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'venta' : venta, 'no_es_vendedor':es_vendedor}
        if formPago.is_valid():
            data = formPago.cleaned_data
            monto = data['monto']
            if venta.monto_acumulado + monto > venta.monto_total:
                formPago.errors['monto'] = ErrorList(['El monto acumulado no puede ser mayor al monto total de la venta.'])
                forms = {'formPago':formPago, 'venta' : venta, 'no_es_vendedor':es_vendedor}
                return render(request, 'cotizaciones/registrar_pago.html', forms)
            else:
                venta.monto_acumulado += monto
                if venta.monto_acumulado >= venta.monto_total:
                    venta.is_completada = True
                venta.save()
                Pago(monto=monto, venta=venta).save()
                return render(request, 'principal/exito.html')
    else:
        formPago = PagoForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'no_es_vendedor':es_vendedor, 'venta' : venta}
    return render(request, 'cotizaciones/registrar_pago.html', forms)

@login_required
def eliminar_cotizacion(request, id_cotizacion):
    cotizacion = Cotizacion.objects.get(pk=id_cotizacion)
    cotizacion.is_active = False
    cotizacion.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
def eliminar_venta(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    venta.is_active = False
    venta.save()
    es_vendedor = no_es_vendedor(request.user)
    return render(request, 'principal/exito.html', {'no_es_vendedor':es_vendedor})

@login_required
def editar_cotizacion(request, id_cotizacion):
    """ Vista para editar una cotizacion.
    """
    cotizacion = Cotizacion.objects.get(pk=id_cotizacion)
    current_user = request.user
    current_vendedor = Vendedor.objects.get(user=current_user)
    contactos_list = obtener_contactos_list(current_vendedor)
    contactos_list = obtener_contactos_ids(contactos_list)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = Pozo.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor, 'cotizacion':cotizacion}
        if formCotizacion.is_valid():
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            cotizacion.contacto = contacto
            cotizacion.monto = monto
            cotizacion.descripcion = descripcion
            cotizacion.save()
            return render(request, 'principal/exito.html')
    else:
        formCotizacion = CotizacionForm(instance=cotizacion)
        formCotizacion.fields["contacto"].queryset = Pozo.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor, 'cotizacion':cotizacion}
    return render(request, 'cotizaciones/editar_cotizacion.html', forms)

@login_required
def editar_venta(request, id_venta):
    """ Vista para editar una cotizacion.
    """
    venta = Venta.objects.get(pk=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formVenta = VentaForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'venta':venta}
        if formVenta.is_valid():
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            venta.monto_total = monto_total
            venta.save()
            return render(request, 'principal/exito.html')
    else:
        formVenta = VentaForm(instance=venta)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'venta':venta}
    return render(request, 'cotizaciones/editar_venta.html', forms)

@login_required
def registrar_proveedor(request):
    es_vendedor = no_es_vendedor(request.user)
    if request.method == 'POST':
        formProveedor = ProveedorForm(request.POST)
        forms = {'formProveedor':formProveedor, 'no_es_vendedor':es_vendedor}
        if formProveedor.is_valid():
            data = formProveedor.cleaned_data
            nombre = data['nombre']
            telefono = data['telefono']
            proveedor = Proveedor(nombre=nombre, telefono=telefono)
            proveedor.save()
            return render(request, 'principal/exito.html')
    else:
        formProveedor = ProveedorForm()
        forms = {'formProveedor':formProveedor, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_proveedor.html', forms)

@login_required
def proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {}
    context['proveedores'] = proveedores
    return render(request, 'cotizaciones/proveedores.html', context)

@login_required
def proveedor(request, id_proveedor):
    """ Vista para mostrar el detalle de una proveedor.
    """
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    proveedor_vende_productos = Vende.objects.filter(proveedor=proveedor)
    proveedor_brinda_servicios = Brinda.objects.filter(proveedor=proveedor)
    # productos
    # servicios
    print('proveedor')
    context = {}
    context['proveedor'] = proveedor
    context['proveedor_vende_productos'] = proveedor_vende_productos
    context['proveedor_brinda_servicios'] = proveedor_brinda_servicios
    return render(request, "cotizaciones/proveedor.html", context)

@login_required
def editar_proveedor(request, id_proveedor):
    return redirect('proveedor', id_proveedor=id_proveedor)

@login_required
def eliminar_proveedor(request, id_proveedor):
    return redirect('proveedor', id_proveedor=id_proveedor)

@login_required
def registrar_producto(request):
    es_vendedor = no_es_vendedor(request.user)
    if request.method == 'POST':
        formProducto = ProductoForm(request.POST)
        forms = {'formProducto':formProducto, 'no_es_vendedor':es_vendedor}
        if formProducto.is_valid():
            data = formProducto.cleaned_data
            nombre = data['nombre']
            lugar = data['lugar']
            cantidad = data['cantidad']
            producto = Producto(nombre=nombre, lugar=lugar, cantidad=cantidad)
            producto.save()
            return render(request, 'principal/exito.html')
    else:
        formProducto = ProductoForm()
        forms = {'formProducto':formProducto, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_producto.html', forms)

@login_required
def productos(request):
    productos = Producto.objects.all()
    context = {}
    context['productos'] = productos
    return render(request, 'cotizaciones/productos.html', context)

@login_required
def producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    context = {}
    context['producto'] = producto
    return render(request, 'cotizaciones/producto.html', context)
"""
@login_required
def cotizacion(request, id_cotizacion):

    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    contacto = cotizacion.contacto
    pertenece = Pertenece.objects.get(contacto=contacto)
    es_vendedor = no_es_vendedor(request.user)

    context = {}
    context['cotizacion'] = cotizacion
    context['contacto'] = contacto
    context['pertenece'] = pertenece
    context['no_es_vendedor'] = es_vendedor
    return render(request, "cotizaciones/cotizacion.html", context)
"""

@login_required
def registrar_servicio(request):
    es_vendedor = no_es_vendedor(request.user)
    if request.method == 'POST':
        formServicio = ServicioForm(request.POST)
        forms = {'formServicio':formServicio, 'no_es_vendedor':es_vendedor}
        if formServicio.is_valid():
            data = formServicio.cleaned_data
            nombre = data['nombre']
            servicio = Servicio(nombre=nombre)
            servicio.save()
            return render(request, 'principal/exito.html')
    else:
        formServicio = ServicioForm()
        forms = {'formServicio':formServicio, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_servicio.html', forms)

@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    context = {}
    context['servicios'] = servicios
    return render(request, 'cotizaciones/servicios.html', context)

@login_required
def registrar_vende(request):
    es_vendedor = no_es_vendedor(request.user)
    if request.method == 'POST':
        formVende = VendeForm(request.POST)
        forms = {'formVende':formVende, 'no_es_vendedor':es_vendedor}
        if formVende.is_valid():
            data = formVende.cleaned_data
            proveedor = data['proveedor']
            producto = data['producto']
            precio = data['precio']
            vende = Vende(proveedor=proveedor, producto=producto, precio=precio)
            vende.save()
            return render(request, 'principal/exito.html')
    else:
        formVende = VendeForm()
        forms = {'formVende':formVende, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_proveedor_vende_producto.html', forms)

@login_required
def registrar_brinda(request):
    es_vendedor = no_es_vendedor(request.user)
    formBrinda = BrindaForm()
    forms = {'formBrinda':formBrinda, 'no_es_vendedor':es_vendedor}
    return render(request, 'cotizaciones/registrar_proveedor_brinda_servicio.html', forms)
