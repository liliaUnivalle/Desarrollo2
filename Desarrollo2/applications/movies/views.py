# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import models
from applications.users.models import Usuario
from applications.movies.models import *
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
import tmdbsimple as tmdb
import sys
from numpy import *
#Cambiar por el directorio en el que se encuentre el archivo clasePelicula

#Definicion de la key
tmdb.API_KEY = 'ce6b4a15c201b1ccc831cf754f9579cc'

class PeliculaAPI:

	def __init__(self, id, titulo, imagen, descripcion, fecha_estreno,trailer,reviews,generos):
		self.id = id
		self.titulo = titulo
		self.imagen = imagen
		self.descripcion = descripcion
		self.fecha_estreno = fecha_estreno
		self.trailer = trailer
		self.reviews = reviews
		self.generos = generos

def crearPeliculaBD(json, tipo):
	
	id = str(json['id'])	
	imagenJson = str(json['poster_path'])
	imagen1 = 'http://image.tmdb.org/t/p/w342' + imagenJson
	pelicula = Pelicula(
		codigo = str(id),
		titulo = json['title'],
		imagen = imagen1,
		descripcion = json['overview'],
		trailer = extraerTrailer(id),
		fechaEstreno = str(json['release_date']),
		)
	pelicula.save()
	extraerReviewsBD(id, pelicula)
	extraerGeneroBD(json['genre_ids'], pelicula)
	tipo_p = Tipo.objects.get(nombre=tipo)
	pelicula.tipos.add(tipo_p)

	return pelicula
	

def extraerReviewsBD(id, pelicula):
	movie = tmdb.Movies(id)
	criticas = movie.reviews()
	#print(criticas)

	if criticas['total_results'] != 0:
		#Primer campo autor, segundo contenido
		for n in movie.results:
			critica = Critica_calificacion(
			 critico = n['author'],
			 critica_calificacion = n['content'],
			 )

			critica.save()
			pelicula.criticas.add(critica)

def extraerGeneroBD(genres, pelicula):
	if len(genres) != 0:

		objGenero = tmdb.Genres()
		lista = objGenero.list()

		for n in genres:
			for f in objGenero.genres:
				if f['id'] == n:
					genero = Genero.objects.get(id_genero= f['id'])
					pelicula.generos.add(genero)


def extraerTrailer(id):
	movie = tmdb.Movies(id)
	videitos = movie.videos()
	n = movie.results
	link = 'https://www.youtube.com/watch?v='
	if len(n) != 0:
		finalLink = n[0]['key']		
		linkDefinitivo = link + finalLink

		return linkDefinitivo

	return link


def consultarTendencia(x):
	numPelis = x

	movie = tmdb.Movies()
	tendencia = movie.popular()
	tipo_p = Tipo.objects.get(nombre="Tendencia")
	for n in movie.results:

		if numPelis < 1:
			break
		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			crearPeliculaBD(n, "Tendencia")

def consultarEnCartelera(x):
	tipo_p = Tipo.objects.get(nombre="Cartelera")
	movie = tmdb.Movies()
	estreno = movie.now_playing()

	for n in movie.results:

		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			crearPeliculaBD(n, "Cartelera")

		numPelis = numPelis - 1

def consultarEstrenos():
	tipo_p = Tipo.objects.get(nombre="Estrenos")
	movie = tmdb.Movies()
	estreno = movie.upcoming()
	
	for n in movie.results:
		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			pelicula = crearPeliculaBD(n, "Estrenos")


def listasPeliculas():
	listas = []	
	tendencias = [0]*4
	for i in range(4):		
		tendencias[i] = Pelicula.objects.filter(tipos="Tendencia")[i]
	ten = {'nombre':"Tendencias", 'lista':tendencias}
	listas.append(ten)	

	cartelera = [0]*4
	for i in range(4):		
		cartelera[i] = Pelicula.objects.filter(tipos="Cartelera")[i]
	ten2 = {'nombre':"En Cartelera", 'lista':cartelera}
	listas.append(ten2)

	estrenos = [0]*4
	for i in range(4):		
		estrenos[i] = Pelicula.objects.filter(tipos="Estrenos")[i]
	ten3 = {'nombre':"Estrenos", 'lista':estrenos}
	listas.append(ten3)

	return listas

def consultaPorTitulo(titulo):

	search = tmdb.Search()
	response = search.movie(query=titulo)
	peliculasTitulo= []

	if search.total_results != 0:

		for n in search.results:
			try:
				pelicula_p = Pelicula.objects.get(codigo=n)
				peliculasTitulo.append(pelicula_p)
			except:
				peliculasTitulo.append(crearPeliculaBD(n, "Regular"))

	return peliculasTitulo

def calificacion(codigo, email, valor):
	calificacion = Calificacion(
		codigo = codigo,
		email = email,
		valor = valor,
		)
	calificacion.save()

#Templates-------------------------------------------------------------------------------------------------
class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class TendenciaCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarTendencia(90)
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class CarteleraCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarEnCartelera(90)
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class EstrenosCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarEstrenos()
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class Inicio(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = listasPeliculas()
		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Tendencias(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		tendencias = Pelicula.objects.filter(tipos="Tendencia")
		ten = {'nombre':"Tendencias", 'lista':tendencias}
		listas.append(ten)
		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Cartelera(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		cartelera = Pelicula.objects.filter(tipos="Cartelera")
		ten = {'nombre':"En Cartelera", 'lista':cartelera}
		listas.append(ten)
		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Estrenos(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		estrenos = Pelicula.objects.filter(tipos="Estrenos")
		ten = {'nombre':"Estrenos", 'lista':estrenos}
		listas.append(ten)
		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class VerMas(TemplateView):
	def get(self,request,*args, **kwargs):

		try:
			pelicula = Pelicula.objects.get(codigo=args[0])
		except:
			pelicula = None

		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

class Busqueda(TemplateView):
	def get(self,request,*args, **kwargs):
		actor = request.POST['actor']
		titulo = request.POST['titulo']
		if(titulo != ""):
			nombre = request.session['emailUser']
			authentication = True
			listas = consultaPorTitulo(titulo) 
			context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
			return render_to_response(
				'movies/inicio.html',
				context,
				context_instance=RequestContext(request))
		else:
			nombre = request.session['emailUser']
			authentication = True
			context={'authentication':authentication, 'nombre':nombre, }
			return render_to_response(
				'movies/inicio.html',
				context,
				context_instance=RequestContext(request))


class Prueba(TemplateView):
	def get(self,request,*args, **kwargs):
		lol = "r"
		l = "apsito"
		pelicula = Usuario(
			email="dhurvrfb",
			nombre="mateo",
			contrasena="1234567",
			tipo="admin"
			)
		pelicula.save()

		context = {'lol':lol, 'l':l, 'pelicula':pelicula}
		return render_to_response(

			'movies/movie.html',context,
			context_instance=RequestContext(request))

class Index(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre}
		return render_to_response(

			'movies/inicio.html',context,
			context_instance=RequestContext(request))