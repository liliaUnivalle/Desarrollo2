from __future__ import unicode_literals

from django.db import models
from applications.movies.models import Pelicula
from applications.movies.models import Genero
from datetime import datetime

# Create your models here.

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
		return ",".join([str(p.codigo) for p in self.contenido.all()])

	class Meta:
		unique_together = ('nombre', 'email')
		verbose_name = 'Lista_personal'
		verbose_name_plural = 'Listas_personales'


class Coleccion(models.Model):
	email = models.OneToOneField(Usuario, primary_key=True,related_name="lista4_1")
	contenido = models.ManyToManyField(Pelicula)

	def get_email(self):
		return self.email.email

	def get_contenido(self):
		return ",".join([str(p.codigo) for p in self.contenido.all()])

	class Meta:
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
		
	def get_pelicula(self):
		return self.codigo.codigo
	def get_email(self):
		return self.email.email

class FechaPeliculaVista(models.Model):
	codigo = models.ForeignKey(Pelicula, related_name="fecha")
	email = models.ForeignKey(Usuario, related_name="fecha")
	fecha = models.DateField(null=True,blank=True)

	class Meta:
		unique_together = ('codigo', 'email')
		verbose_name = 'FechaPeliculaVista'
		verbose_name_plural = 'FechasPeliculasVistas'
		
	def get_pelicula(self):
		return self.codigo.codigo
	def get_email(self):
		return self.email.email

class Cine(models.Model):
	nombre = models.CharField(max_length=100,primary_key=True)

class CineVista(models.Model):
	codigo = models.ForeignKey(Pelicula, related_name="cineVista")
	email = models.ForeignKey(Usuario, related_name="cineVista")
	cine = models.ForeignKey(Cine, related_name="cineVista")

	class Meta:
		unique_together = ('codigo', 'email')
		verbose_name = 'CineVista'
		verbose_name_plural = 'CineVistas'
		
	def get_pelicula(self):
		return self.codigo.codigo
	def get_email(self):
		return self.email.email
	def get_cine(self):
		return self.cine.nombre

