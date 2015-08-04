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
