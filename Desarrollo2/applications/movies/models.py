
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pelicula(models.Model):
	codigo = models.CharField(max_length=10,primary_key=True)
	titulo = models.CharField(max_length=100,null=True,blank=True)
	imagen = models.CharField(max_length=500,null=True,blank=True)
	descripcion = models.CharField(max_length=100,null=True,blank=True)
	an_o = models.CharField(max_length=100,null=True,blank=True)
	trailer = models.CharField(max_length=100,null=True,blank=True)
	fecha_estreno = models.CharField(max_length=100,null=True,blank=True)

class Actores(models.Model):
	codigo = models.ForeignKey(Pelicula)
	actor = models.CharField(max_length=100,null=True,blank=True)
	
	class Meta:
		unique_together = ('codigo','actor')

class Critica_calificacion(models.Model):
	codigo = models.ForeignKey(Pelicula)
	Critica_calificacion = models.CharField(max_length=700,null=True,blank=True)
	critico = models.CharField(max_length=100,null=True,blank=True)
