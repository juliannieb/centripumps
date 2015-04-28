from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date

from cotizaciones.models import Cotizacion, Venta, Pago
from principal.models import Vendedor
from contactos.models import Pertenece

from cotizaciones.forms import Contacto, CotizacionForm, VentaForm, PagoForm

def no_es_vendedor(user):
    """ Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

@login_required
def consultar_cotizaciones(request):
    """ Vista para mostrar todas las cotizaciones de un usuario.
    """
    current_user = request.user
    if no_es_vendedor(current_user):
        cotizaciones_list = Cotizacion.objects.all()
    else:
        current_vendedor = Vendedor.objects.get(user=current_user)
        todos_los_contactos = Contacto.objects.all()
        contactos_list = []
        for contacto in todos_los_contactos:
            if contacto.atiende_set.all():
                if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor == current_vendedor:
                    contactos_list.append(contacto)

        todas_las_cotizaciones = Cotizacion.objects.all()
        todas_las_ventas = Venta.objects.all()
        cotizaciones_list = []

        for cotizacion in todas_las_cotizaciones:
            for contacto in contactos_list:
                if cotizacion.contacto == contacto and cotizacion.fecha_creacion >= contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].fecha:
                    cotizaciones_list.append(cotizacion)

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
        todos_los_contactos = Contacto.objects.all()
        contactos_list = []
        for contacto in todos_los_contactos:
            if contacto.atiende_set.all():
                if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor == current_vendedor:
                    contactos_list.append(contacto)

        todas_las_cotizaciones = Cotizacion.objects.all()
        todas_las_ventas = Venta.objects.all()
        cotizaciones_list = []
        ventas_list = []

        for cotizacion in todas_las_cotizaciones:
            for contacto in contactos_list:
                if cotizacion.contacto == contacto and cotizacion.fecha_creacion >= contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].fecha:
                    cotizaciones_list.append(cotizacion)

        for venta in todas_las_ventas:
            for cotizacion in cotizaciones_list:
                if venta.cotizacion == cotizacion:
                    ventas_list.append(venta)


        #cotizaciones_list = Cotizacion.objects.filter(contacto=contactos_list)
        #ventas_list = Venta.objects.filter(cotizacion=cotizaciones_list)
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
    todos_los_contactos = Contacto.objects.all()
    contactos_list = []
    for contacto in todos_los_contactos:
        if contacto.atiende_set.all():
            if contacto.atiende_set.all()[len(contacto.atiende_set.all()) - 1].vendedor == current_vendedor:
                contactos_list.append(contacto.pk)
    if request.method == 'POST':
        formCotizacion = CotizacionForm(request.POST)
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formCotizacion.is_valid():
            # Save the new category to the database.
            data = formCotizacion.cleaned_data
            contacto = data['contacto']
            monto = data['monto']
            descripcion = data['descripcion']
            Cotizacion(contacto=contacto, monto=monto, descripcion=descripcion).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formCotizacion.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formCotizacion = CotizacionForm()
        formCotizacion.fields["contacto"].queryset = Contacto.objects.filter(pk__in=contactos_list)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formCotizacion':formCotizacion, 'no_es_vendedor':es_vendedor}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
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

        # Have we been provided with a valid form?
        if formVenta.is_valid():
            # Save the new category to the database.
            data = formVenta.cleaned_data
            monto_total = data['monto_total']
            cotizacion.is_pendiente = False
            cotizacion.save()
            Venta(monto_total=monto_total, cotizacion=cotizacion).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formVenta.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formVenta = VentaForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formVenta':formVenta, 'no_es_vendedor':es_vendedor, 'cotizacion' : cotizacion}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_venta.html', forms)


@login_required
def registrar_pago(request, id_venta):
    venta = Venta.objects.get(id=id_venta)
    current_user = request.user
    if request.method == 'POST':
        formPago = PagoForm(request.POST)
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'venta' : venta, 'no_es_vendedor':es_vendedor}

        # Have we been provided with a valid form?
        if formPago.is_valid():
            # Save the new category to the database.
            data = formPago.cleaned_data
            monto = data['monto']
            venta.monto_acumulado += monto
            if venta.monto_acumulado >= venta.monto_total:
                venta.is_completada = True
            venta.save()
            Pago(monto=monto, venta=venta).save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/exito.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (formPago.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formPago = PagoForm()
        es_vendedor = no_es_vendedor(request.user)
        forms = {'formPago':formPago, 'no_es_vendedor':es_vendedor, 'venta' : venta}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'cotizaciones/registrar_pago.html', forms)
