from django.contrib import admin

from empresas.models import Cliente, RedSocial, Estado, Municipio, Direccion
from empresas.models import TipoRedSocial, ClienteTieneDireccion

admin.site.register(Cliente)
admin.site.register(TipoRedSocial)
admin.site.register(RedSocial)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(ClienteTieneDireccion)
