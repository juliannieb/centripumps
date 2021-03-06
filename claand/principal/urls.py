from django.conf.urls import url, patterns
from principal import views
from django.conf.urls.static import static

urlpatterns = patterns('',
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^index/$', views.index, name='index'),
        url(r'^consultar/$', views.consultar, name='consultar'),
        url(r'^global/$', views.consultar_global, name='consultar_global'),

        url(r'^vendedores/$', views.consultar_vendedores, name='consultar_vendedores'),
        url(r'^vendedores/(?P<id_vendedor>[\w\-]+)/$', views.vendedor, name='vendedor'),
        url(r'^registrar_vendedor/$', views.registrar_vendedor, name='registrar_vendedor'),
        url(r'^eliminar-vendedor/(?P<id_vendedor>[\w\-]+)/$', views.eliminar_vendedor, \
            name="eliminar_vendedor"),
        #url(r'^director/$', views.director_index, name='director_index'),
        )


