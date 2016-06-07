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