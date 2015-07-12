from django import forms
from Repositorio3D.modelos3D.models import Model3D


class CrearModelo3DForm(forms.ModelForm):

    class Meta:
        model = Model3D
        fields = ('nombre', 'descripcion', 'valoracion')
