from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from empresas.forms import EmpresaForm, DireccionForm, NumeroTelefonicoForm, RedSocialForm
from empresas.models import Empresa, Direccion, EmpresaTieneDireccion


@login_required
def consultar_empresas(request):
    """ mostrar todas las empresas """
    empresas_list = Empresa.objects.all()
    return render(request, 'empresas/empresas.html', {'empresas_list': empresas_list})

@login_required
def empresa(request, empresa_nombre_slug):
    """ mostrar una empresa """
    empresa = Empresa.objects.get(slug=empresa_nombre_slug)
    empresa_tiene_direccion = EmpresaTieneDireccion.objects.filter(empresa=empresa)
    numeros_list = empresa.numerotelefonico_set.all()
    redes_list = empresa.redsocial_set.all()
    return render(request, 'empresas/empresa.html', {'empresa': empresa, 'empresa_tiene_direccion': empresa_tiene_direccion,'numeros_list': numeros_list, 'redes_list': redes_list})

@login_required
def registrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        formDireccion = DireccionForm(request.POST)
        formNumeroTelefonico = NumeroTelefonicoForm(request.POST)
        formRedSocial = RedSocialForm(request.POST)
        forms = {'form':form, 'formDireccion':formDireccion, 'formNumeroTelefonico':formNumeroTelefonico, 'formRedSocial':formRedSocial}

        # Have we been provided with a valid form?
        if form.is_valid() and formDireccion.is_valid() and formNumeroTelefonico.is_valid() and formRedSocial.is_valid():
            # Save the new category to the database.
            empresa = form.instance
            empresa = form.save(commit=True)
            direccion = formDireccion.save(commit=True)

            EmpresaTieneDireccion(empresa=empresa, direccion=direccion).save()

            if formNumeroTelefonico.has_changed():
                numero_telefonico = formNumeroTelefonico.instance
                numero_telefonico.empresa = empresa
                numero_telefonico.save()
            if formRedSocial.has_changed():
                red_social = formRedSocial.instance
                red_social.empresa = empresa
                red_social.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'principal/index_vendedor.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
            print (formDireccion.errors)
            print (formNumeroTelefonico.errors)
            print (formRedSocial.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = EmpresaForm()
        formDireccion = DireccionForm()
        formNumeroTelefonico = NumeroTelefonicoForm()
        formRedSocial = RedSocialForm()
        forms = {'form':form, 'formDireccion':formDireccion, 'formNumeroTelefonico':formNumeroTelefonico, 'formRedSocial':formRedSocial}

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'empresas/registrar_empresa2.html', forms)
