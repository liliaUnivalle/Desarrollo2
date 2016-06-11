from __future__ import unicode_literals

from django.db import models
from applications.movies.models import Pelicula
from datetime import datetime

# Create your models here.

class Genero(models.Model):
	id_genero = models.CharField(max_length=10,primary_key=True)
	
class Usuario(models.Model):
	email = models.CharField(max_length=100,primary_key=True)
	nombre = models.CharField(max_length=100,null=True,blank=True)
	contrasena = models.CharField(max_length=100,null=True,blank=True)
	tipo = models.CharField(max_length=100,null=True,blank=True)
	generos = models.ManyToManyField(Genero)
	lista_peliculas_porver = models.ManyToManyField(Pelicula, related_name="lista_porver")
	lista_peliculas_vistas = models.ManyToManyField(Pelicula, related_name="lista_vistas")

	def get_generos(self):
		return ",".join([str(p.id_genero) for p in self.generos.all()])

	def get_porver(self):
		return ",".join([str(p.codigo) for p in self.lista_peliculas_porver.all()])

	def get_vistas(self):
		return ",".join([str(p.codigo) for p in self.lista_peliculas_vistas.all()])



class Lista_personal(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.ForeignKey(Usuario, related_name="lista3_1")
	contenido = models.ManyToManyField(Pelicula)

	def get_contenido(self):
		return ",".join([str(p.nombre) for p in self.contenido.all()])

	class Meta:
		unique_together = ('nombre', 'email')
		verbose_name = 'Lista_personal'
		verbose_name_plural = 'Listas_personales'


class Coleccion(models.Model):
	id_genero = models.ForeignKey(Genero, related_name="li")
	email = models.ForeignKey(Usuario, related_name="lista4_1")
	contenido = models.ManyToManyField(Pelicula)

	def get_contenido(self):
		return ",".join([str(p.nombre) for p in self.contenido.all()])

	class Meta:
		unique_together = ('id_genero', 'email')
		verbose_name = 'Coleccion'
		verbose_name_plural = 'Colecciones'


class Calificacion(models.Model):
	codigo = models.ForeignKey(Pelicula, related_name="califica")
	email = models.ForeignKey(Usuario, related_name="califica")
	valor_Calificacion = models.IntegerField(null=True,blank=True)

	class Meta:
		unique_together = ('codigo', 'email')
		verbose_name = 'Calificacion'
		verbose_name_plural = 'Calificaciones'

class Consulta():

	def listar_peliculas_vistas(self, usuario):
		lista = Lista_peliculas_vistas.object.filter(email=usuario)
		return lista

