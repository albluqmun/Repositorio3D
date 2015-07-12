#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


# falta la sección comentarios y visualizar el mdoelo 3D
class Model3D(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    valoracion = models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __unicode__(self):
        return u'%s - %s' % (self.nombre, self.descripcion)

    def get_absolute_url(self):
        return reverse('index')


class ImagenesModelos(models.Model):
    modelo = models.ForeignKey('Model3D')
    imagen = models.ImageField()


class TagsModelos(models.Model):
    modelo = models.ForeignKey('Model3D')
    tag = models.CharField(max_length=50)
