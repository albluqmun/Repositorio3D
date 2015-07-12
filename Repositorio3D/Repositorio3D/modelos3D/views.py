from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from Repositorio3D.modelos3D.models import Model3D
from Repositorio3D.modelos3D.forms import CrearModelo3DForm


class Index(TemplateView):
    template_name = 'modelos3D/index.html'


class ListaModelos(ListView):
    model = Model3D
    template_name = 'modelos3D/lista_modelos.html'


class VerModelo(DetailView):
    model = Model3D
    pk_url_kwarg = 'modelo_id'
    template_name = 'modelos3D/detalle_modelo.html'


class CrearModelo(CreateView):
    form_class = CrearModelo3DForm
    template_name = 'modelos3D/crear_modelo.html'


class ModificarModelo(UpdateView):
    form_class = CrearModelo3DForm
    model = Model3D
    pk_url_kwarg = 'modelo_id'
    template_name = 'modelos3D/actualizar_modelo.html'


class EliminarModelo(DeleteView):
    model = Model3D
    pk_url_kwarg = 'modelo_id'
    success_url = reverse_lazy('index')
