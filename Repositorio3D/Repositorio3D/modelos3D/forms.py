#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from django import forms
from Repositorio3D.modelos3D.models import Model3D, ImagenesModelos, TagsModelos


class CrearModelo3DForm(forms.ModelForm):

    class Meta:
        model = Model3D
        fields = ('nombre', 'descripcion')


class ImagenesModelosForm(forms.ModelForm):

    class Meta:
        model = ImagenesModelos
        fields = ('imagen',)


class TagsModelosForm(forms.ModelForm):

    class Meta:
        model = TagsModelos
        fields = ('tag',)

    def clean(self):
        # traducciones
        patron = re.compile(r'^([0-9a-zA-Z_ñÑáÁéÉíÍóÓúÚ,]+\s*)+$')
        if patron.match(self.cleaned_data.get('tag').encode('utf8')) is None:
            raise forms.ValidationError("Sólo se permiten caracteres alfanuméricos y _ sin empezar por espacios en blanco")
        return self.cleaned_data


class CreateTagForm(forms.ModelForm):
    modelo = forms.ModelChoiceField(queryset=Model3D.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = TagsModelos
        fields = ('tag','modelo')

    def __init__(self, *args, **kwargs):
        modelo = kwargs.pop('modelo', None)
        super(CreateTagForm, self).__init__(*args, **kwargs)
        if modelo:
            self.fields['modelo'].initial = modelo

    def clean(self):
        # traducciones
        patron = re.compile(r'^([0-9a-zA-Z_ñÑáÁéÉíÍóÓúÚ]+\s*)+$')
        if patron.match(self.cleaned_data.get('tag').encode('utf8')) is None:
            raise forms.ValidationError("Sólo se permiten caracteres alfanuméricos y _ sin empezar por espacios en blanco")
        return self.cleaned_data
