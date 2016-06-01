# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import models
from applications.movies.models import Pelicula
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT

class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class Prueba(TemplateView):
	def get(self,request,*args, **kwargs):
		lol = "r"
		l = "apsito"
		pelicula = Pelicula(
			codigo=1,
			titulo="lol",
			imagen="1.jpeg",
			descripcion="ejhfawegbsrhag",
			an_o="2016",
			trailer="este es un trailer",
			fecha_estreno="11 abril 2017"
			)
		pelicula.save()

		context = {'lol':lol, 'l':l, 'pelicula':pelicula}
		return render_to_response(

			'movies/movie.html',context,
			context_instance=RequestContext(request))