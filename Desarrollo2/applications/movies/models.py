
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pelicula(models.Model):
	codigo = models.CharField(max_length=10,primary_key=True)

class Critica_calificacion(models.Model):
	codigo = models.ForeignKey(Pelicula)
	Critica_calificacion = models.CharField(max_length=700,null=True,blank=True)
	critico = models.CharField(max_length=100,null=True,blank=True)
