
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tipo(models.Model):
	nombre = models.CharField(max_length=10,primary_key=True)

class Genero(models.Model):
	id_genero = models.CharField(max_length=10,primary_key=True)
	nombre = models.CharField(max_length=70,blank=True)


class Critica_calificacion(models.Model):
	critica_calificacion = models.CharField(max_length=1700,null=True,blank=True)
	critico = models.CharField(max_length=100,null=True,blank=True)

	class Meta:
		unique_together = ('critico', 'critica_calificacion')
		verbose_name = 'Critica_calificacion'
		verbose_name_plural = 'Criticas_calificaciones'


class Actor(models.Model):
	nombre = models.CharField(max_length=10,primary_key=True)


class Pelicula(models.Model):
	codigo = models.CharField(max_length=30,primary_key=True)
	titulo = models.CharField(max_length=100,null=True,blank=True)
	imagen = models.CharField(max_length=700,null=True,blank=True)
	descripcion = models.CharField(max_length=1500,null=True,blank=True)  
	trailer = models.CharField(max_length=700,null=True,blank=True)
	fechaEstreno = models.CharField(max_length=50,null=True,blank=True)
	criticas = models.ManyToManyField(Critica_calificacion)
	generos = models.ManyToManyField(Genero)
	tipos = models.ManyToManyField(Tipo)
	actores = models.ManyToManyField(Actor)


	def get_criticas(self):
		return ",".join([str(p.critico) for p in self.criticas.all()])

	def get_generos(self):
		return ",".join([str(p.id_genero) for p in self.generos.all()])

	def get_tipos(self):
		return ",".join([str(p.nombre) for p in self.tipos.all()])

	def get_actores(self):
		return ",".join([str(p.nombre) for p in self.actores.all()])

	def basic_info_to_json(self):
		return json.dumps(
			{
			'codigo':self.codigo
			}
		)

