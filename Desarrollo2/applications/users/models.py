from __future__ import unicode_literals

from django.db import models
from applications.movies.models import Pelicula

# Create your models here.
class Usuario(models.Model):
	email = models.CharField(max_length=100,primary_key=True)
	nombre = models.CharField(max_length=100,null=True,blank=True)
	contrasena = models.CharField(max_length=100,null=True,blank=True)

class Auditor(models.Model):
	email = models.ForeignKey(Usuario, related_name="auditor", primary_key=True)
	nombre = models.ForeignKey(Usuario, related_name="auditor2")
	contrasena = models.ForeignKey(Usuario, related_name="auditor3")
	documento_id = models.CharField(max_length=15,null=True,blank=True)

class Cliente(models.Model):
	email = models.ForeignKey(Usuario, related_name="cliente1",primary_key=True)
	nombre = models.ForeignKey(Usuario, related_name="cliente2")
	contrasena = models.ForeignKey(Usuario)

class Lista_peliculas_porver(models.Model):
	email = models.ForeignKey(Cliente, related_name="lista1_1")
	codigo = models.ForeignKey(Pelicula, related_name="lista1_2")

	class Meta:
		unique_together = ('email', 'codigo')

class Lista_peliculas_vistas(models.Model):
	email = models.ForeignKey(Cliente, related_name="lista2_1")
	codigo = models.ForeignKey(Pelicula, related_name="lista2_1")

	class Meta:
		unique_together = ('email', 'codigo')

class Categorias_favoritas(models.Model):
	email = models.ForeignKey(Usuario,related_name="cat1", primary_key=True)
	categoria = models.CharField(max_length=50,null=True,blank=True)

class Lista_personal(models.Model):
	nombre = models.CharField(max_length=100, primary_key = True)
	email = models.ForeignKey(Cliente, related_name="lista3_1")

class Contiene(models.Model):
	nombre = models.ForeignKey(Lista_personal, related_name="cont1")
	codigo = models.ForeignKey(Pelicula, related_name="cont2")

	class Meta:
		unique_together = ('nombre', 'codigo')

class Califica(models.Model):
	codigo = models.ForeignKey(Pelicula, related_name="califica")
	email = models.ForeignKey(Cliente, related_name="califica")
	valor_Calificacion = models.IntegerField(max_length=1,null=True,blank=True)

	class Meta:
		unique_together = ('codigo', 'email')

class Consulta():

	def listar_peliculas_vistas(self, usuario):
		lista = Lista_peliculas_vistas.object.filter(email=usuario)
		return lista