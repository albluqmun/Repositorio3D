#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

fs = FileSystemStorage(location='Repositorio3D/media/imagenes')


# falta la sección comentarios y visualizar el mdoelo 3D
class Model3D(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    valoracion = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.descripcion)

    def get_absolute_url(self):
        return reverse('index')

    def get_imagenes(self):
        return self.imagenesmodelos_set.filter()

    def get_tags(self):
        return self.tagsmodelos_set.filter()

    class Meta:
        verbose_name = 'Modelo 3D'
        verbose_name_plural = 'Modelos 3D'


class ImagenesModelos(models.Model):
    modelo = models.ForeignKey('Model3D')
    imagen = models.ImageField(storage=fs)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'


class TagsModelos(models.Model):
    modelo = models.ForeignKey('Model3D')
    tag = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
