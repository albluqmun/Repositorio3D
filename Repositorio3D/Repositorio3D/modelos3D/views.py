# -*- coding: utf-8 -*-
import htmlentitydefs

import os
from datetime import datetime
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from formtools.wizard.views import SessionWizardView

from Repositorio3D.modelos3D.models import Model3D, TagsModelos, ImagenesModelos
from Repositorio3D.modelos3D.forms import CrearModelo3DForm, ImagenesModelosForm, TagsModelosForm
# from Repositorio3D.accounts.views import LoginRequiredMixin


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


# hacer que solo se pueda crear un modelo si estas registrado
class CrearModeloWizard(SessionWizardView):
    template_name = 'modelos3D/crear_modelo_wizard.html'
    form_list = [CrearModelo3DForm, ImagenesModelosForm, TagsModelosForm]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tmp'))

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(CrearModeloWizard, self).dispatch(*args, **kwargs)

    def done(self, form_list, form_dict, **kwargs):
        modelo = form_dict['0']
        modelo_creado = Model3D.objects.create(nombre=modelo.data['0-nombre'], descripcion=modelo.data['0-descripcion'], user=self.request.user)

        actual_time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        imagen_form = form_dict['1']
        imagen_file = imagen_form.files['1-imagen']
        imagen_file.name = '%s-%s%s' % (modelo_creado.nombre, actual_time, os.path.splitext(imagen_file.name)[-1])
        ImagenesModelos.objects.create(modelo=modelo_creado, imagen=imagen_file)

        tags = form_dict['2']
        sequency_tags = str(tags.data['2-tag']).split(',')
        for single_tag in sequency_tags:
            TagsModelos.objects.get_or_create(tag=single_tag.lstrip(), modelo=modelo_creado)

        # esto reenviará a la página del modelo que se acaba de crear
        return HttpResponseRedirect('/crear/')

    def uescape(self, text):
        print repr(text)
        escaped_chars = []
        for c in text:
            if (ord(c) < 32) or (ord(c) > 126):
                c = '&{};'.format(htmlentitydefs.codepoint2name[ord(c)])
            escaped_chars.append(c)
        return ''.join(escaped_chars)


class VerModelosTags(ListView):
    # queryset = Model3D.objects.filter('-publication_date')
    context_object_name = 'modelos'
    pk_url_kwarg = 'tag_name'
    model = Model3D
    template_name = 'modelos3D/lista_tag_modelos.html'

    def get_queryset(self):
        return self.model.objects.filter(tagsmodelos__tag=self.kwargs[self.pk_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super(VerModelosTags, self).get_context_data(**kwargs)
        nombre_tag = self.kwargs[self.pk_url_kwarg]
        context['nombre_tag'] = nombre_tag
        return context
