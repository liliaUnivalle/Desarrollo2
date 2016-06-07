from __future__ import unicode_literals

from django.db import models
from applications.movies.models import Pelicula
from datetime import datetime

# Create your models here.
class Usuario(models.Model):
	email = models.CharField(max_length=100,primary_key=True)
	nombre = models.CharField(max_length=100,null=True,blank=True)
	contrasena = models.CharField(max_length=100,null=True,blank=True)
	tipo = models.CharField(max_length=100,null=True,blank=True)

class Lista_peliculas_porver(models.Model):
	email = models.ForeignKey(Usuario, related_name="lista1_1")
	codigo = models.ForeignKey(Pelicula, related_name="lista1_2")

	class Meta:
		unique_together = ('email', 'codigo')

class Lista_peliculas_vistas(models.Model):
	email = models.ForeignKey(Usuario, related_name="lista2_1")
	codigo = models.ForeignKey(Pelicula, related_name="lista2_1")
	fecha = models.DateField( default=datetime.now())

	class Meta:
		unique_together = ('email', 'codigo')

class Lista_personal(models.Model):
	nombre = models.CharField(max_length=100, primary_key = True)
	email = models.ForeignKey(Usuario, related_name="lista3_1")

class Coleccion(models.Model):
	genero = models.CharField(max_length=100, primary_key = True)
	email = models.ForeignKey(Usuario, related_name="lista4_1")

class Contiene(models.Model):
	nombre = models.ForeignKey(Lista_personal, related_name="cont1")
	codigo = models.ForeignKey(Pelicula, related_name="cont2")
	email = models.ForeignKey(Usuario, related_name="cont3")

	class Meta:
		unique_together = ('nombre', 'codigo', 'email')

class ContieneColeccion(models.Model):
	genero = models.ForeignKey(Contiene, related_name="cont2_1")
	codigo = models.ForeignKey(Pelicula, related_name="cont2_2")
	email = models.ForeignKey(Usuario, related_name="cont2_3")

	class Meta:
		unique_together = ('genero', 'codigo', 'email')

class Califica(models.Model):
	codigo = models.ForeignKey(Pelicula, related_name="califica")
	email = models.ForeignKey(Usuario, related_name="califica")
	valor_Calificacion = models.IntegerField(null=True,blank=True)

	class Meta:
		unique_together = ('codigo', 'email')

class Consulta():

	def listar_peliculas_vistas(self, usuario):
		lista = Lista_peliculas_vistas.object.filter(email=usuario)
		return lista
