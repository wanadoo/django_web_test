# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre_modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_modelo

class Coche(models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.marca,self.modelo)
    class Meta:
        ordering = ('marca',)