from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from Repositorio3D.modelos3D import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'lista_modelos/$', views.ListaModelos.as_view(), name="lista_modelos"),
    url(r'modelos/(?P<modelo_id>\d+)/$', views.VerModelo.as_view(), name="detalle_modelos"),
    url(r'modelos/(?P<modelo_id>\d+)/modificar-descripcion/$', views.ModificarDescripcionModelo.as_view(), name="modificar_descripcion_modelo"),
    url(r'modelos/(?P<modelo_id>\d+)/modificar-titulo/$', views.ModificarNombreModelo.as_view(), name="modificar_nombre_modelo"),
    url(r'modelos/(?P<modelo_id>\d+)/lista-tags/$', views.VerListaTagsModelo.as_view(), name="lista_tag_modelo"),
    url(r'modelos/(?P<modelo_id>\d+)/lista-imagenes/$', views.VerListaImagenesModelo.as_view(), name="lista_imagenes_modelo"),
    url(r'modelos/(?P<modelo_id>\d+)/crear-tag/$', views.CrearTag.as_view(), name="crear_tag"),
    url(r'modelos/(?P<modelo_id>\d+)/subir-imagen/$', views.SubirImagen.as_view(), name="subir_imagen"),
    url(r'modelos/(?P<modelo_id>\d+)/eliminar/$', views.EliminarModelo.as_view(), name="eliminar_modelo"),
    url(r'modelos/nuevo/$', views.CrearModeloWizard.as_view(), name="crear_modelo"),
    url(r'tag/(?P<tag_id>\d+)/eliminar/$', views.EliminarTag.as_view(), name="eliminar_tag"),
    url(r'tag/(?P<tag_name>(\w+\s*)+)/$', views.VerModelosTags.as_view(), name="ver_modelos_tags"),

    # este nombre es muy feo
    url(r'usuario/(?P<user_id>\d+)/mis_modelos$', views.VerMisModelos.as_view(), name="ver_mis_modelos"),

    # VerMisModelos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
