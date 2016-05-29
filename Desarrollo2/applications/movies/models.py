
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