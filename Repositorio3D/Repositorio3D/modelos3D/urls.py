from django.conf.urls import url
from Repositorio3D.modelos3D import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'lista_modelos/$', views.ListaModelos.as_view(), name="lista_modelos"),
    url(r'modelos/(?P<modelo_id>\d+)/$', views.VerModelo.as_view(), name="detalle_modelos"),
    url(r'modelos/(?P<modelo_id>\d+)/modificar/$', views.ModificarModelo.as_view(), name="modificar_modelo"),
    url(r'modelos/(?P<modelo_id>\d+)/eliminar/$', views.EliminarModelo.as_view(), name="eliminar_modelo"),
    url(r'crear/$', views.CrearModeloWizard.as_view(), name="crear_modelo"),
]
