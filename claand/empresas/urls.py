from django.conf.urls import url, patterns
from empresas import views

urlpatterns = patterns('',
        url(r'^registrar/$', views.registrar_empresa, name='registrar_empresa'),
        url(r'^get_municipio/$', views.get_municipio, name='get_municipio'),
        url(r'^consultar/$', views.consultar_empresas, name='consultar_empresas'),
        url(r'^consultar/(?P<cliente_nombre_slug>[\w\-]+)/$', views.cliente, name='cliente'),
        url(r'^search_clientes/$', views.search_clientes, name="search_clientes"),
        )


