from django.conf.urls import url, patterns
from cotizaciones import views

urlpatterns = patterns('',
        url(r'^cotizaciones/$', views.consultar_cotizaciones, name='consultar_cotizaciones'),
        url(r'^cotizaciones/(?P<id_cotizacion>[\w\-]+)/$', views.cotizacion, name='cotizacion'),
        url(r'^ventas/$', views.consultar_ventas, name='consultar_ventas'),
        url(r'^ventas/(?P<id_venta>[\w\-]+)/$', views.venta, name='venta'),
        url(r'^registrar/$', views.registrar, name='registrar_cotizacion'),
        url(r'^cotizaciones/(?P<id_cotizacion>[\w\-]+)/registrar-venta/$', views.registrar_venta, \
            name='registrar_venta'),
        url(r'^ventas/(?P<id_venta>[\w\-]+)/registrar_pago/$', views.registrar_pago, name='registrar_pago'),

        url(r'^eliminar-cotizacion/(?P<id_cotizacion>[\w\-]+)/$', views.eliminar_cotizacion, \
        	name="eliminar_cotizacion"),
        url(r'^eliminar-venta/(?P<id_venta>[\w\-]+)/$', views.eliminar_venta, \
            name="eliminar_venta"),

        url(r'^editar-cotizacion/(?P<id_cotizacion>[\w\-]+)/$', views.editar_cotizacion, \
            name='editar_cotizacion'),
        url(r'^editar-venta/(?P<id_venta>[\w\-]+)/$', views.editar_venta, \
            name='editar_venta'),

        url(r'^registrar_proveedor/$', views.registrar_proveedor, name='registrar_proveedor'),
        url(r'^proveedores/$', views.proveedores, name='proveedores'),
        url(r'^proveedores/(?P<id_proveedor>[\w\-]+)/$', views.proveedor, name='proveedor'),
        url(r'^eliminar-proveedor/(?P<id_proveedor>[\w\-]+)/$', views.eliminar_proveedor, \
        	name="eliminar_proveedor"),
        url(r'^editar-proveedor/(?P<id_proveedor>[\w\-]+)/$', views.editar_proveedor, \
        	name="editar_proveedor"),
        url(r'^registrar_producto/$', views.registrar_producto, name='registrar_producto'),
        url(r'^productos/(?P<id_producto>[\w\-]+)/$', views.producto, name='producto'),
        url(r'^productos/$', views.productos, name='productos'),
        url(r'^eliminar-producto/(?P<id_producto>[\w\-]+)/$', views.eliminar_producto, \
        	name="eliminar_producto"),
        url(r'^editar-producto/(?P<id_producto>[\w\-]+)/$', views.editar_producto, \
        	name="editar_producto"),
        url(r'^registrar_servicio/$', views.registrar_servicio, name='registrar_servicio'),
        url(r'^servicios/$', views.servicios, name='servicios'),
        url(r'^servicios/(?P<id_servicio>[\w\-]+)/$', views.servicio, name='servicio'),
        url(r'^eliminar-servicio/(?P<id_servicio>[\w\-]+)/$', views.eliminar_servicio, \
        	name="eliminar_servicio"),
        url(r'^editar-servicio/(?P<id_servicio>[\w\-]+)/$', views.editar_servicio, \
        	name="editar_servicio"),
        url(r'^registrar_vende/$', views.registrar_vende, name='registrar_vende'),
        url(r'^registrar_brinda/$', views.registrar_brinda, name='registrar_brinda'),
        url(r'^registrar_vende/(?P<id_proveedor>[\w\-]+)/$', views.registrar_vende_proveedor, name='registrar_vende_proveedor'),
        url(r'^registrar_brinda/(?P<id_proveedor>[\w\-]+)/$', views.registrar_brinda_proveedor, name='registrar_brinda_proveedor'),
        )
