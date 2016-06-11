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
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
import tmdbsimple as tmdb
import sys
from numpy import *
#Cambiar por el directorio en el que se encuentre el archivo clasePelicula
sys.path.append('./Desktop')
#Definicion de la key
tmdb.API_KEY = 'ce6b4a15c201b1ccc831cf754f9579cc'

class Pelicula:

	def __init__(self, id, titulo, imagen, descripcion, fecha_estreno,trailer,reviews,generos):
		self.id = id
		self.titulo = titulo
		self.imagen = imagen
		self.descripcion = descripcion
		self.fecha_estreno = fecha_estreno
		self.trailer = trailer
		self.reviews = reviews
		self.generos = generos


def consultaPorGenero(genero):

	peliculasActor = []

	search = tmdb.Search()
	response = search.genre_ids(query=genero)
	
	if search.total_results != 0:

		known = search.results[0]
		knownf = known['known_for']

		print(knownf)

		if len(knownf) != 0:

			for x in knownf:
				pelicula = crearPelicula(x)
				peliculasActor.append(pelicula)

	return peliculasActor

#Templates-------------------------------------------------------------------------------------------------
class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


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
		l
		context = {'lol':lol}
		return render_to_response(

			'movies/inicio.html',context,
			context_instance=RequestContext(request))