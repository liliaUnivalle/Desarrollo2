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
from django.shortcuts import render
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import GetRegister
# Create your views here.
import tmdbsimple as tmdb
import sys
from numpy import *
#Cambiar por el directorio en el que se encuentre el archivo clasePelicula
sys.path.append('./Desktop')
from applications.movies.views import Pelicula
from applications.movies.models import Genero

tmdb.API_KEY = 'ce6b4a15c201b1ccc831cf754f9579cc'


def extraerGeneroTotales():	

	generos = []
	objGenero = tmdb.Genres()
	lista = objGenero.list()
	generosInfo = lista[u'genres']
	for i in generosInfo:
		generos.append(i[u'name'])
	return generos

def extraerGeneroTotalesBD():	

	objGenero = tmdb.Genres()
	lista = objGenero.list()
	generosInfo = lista[u'genres']
	for i in generosInfo:
		genero = Genero (
			nombre = i[u'name']
			)
		genero.save()

#Templates----------------------------------------------------------------------------------
class LoginPage(TemplateView):

	def get(self,request,*args,**kwargs):
		p = request.session['emailUser']
		context={'p':p}
		print p
		return render_to_response(
			context,
			'authentication/login.html', 
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		username = request.POST['username']
		password = request.POST['password']
		print username
		message =""
		messageT = True
		
		try:
			usuario_p = Usuario.objects.get(email=username)
			if(usuario_p.contrasena == password):
				authentication = True		
				nombre = usuario_p.nombre
				request.session['emailUser'] = username		
				context={'authentication':authentication, 'nombre':nombre}
				return render_to_response(
				'movies/movie.html',
				context,
				context_instance = RequestContext(request)
				)
			else:
				message = "La contraseña es invalida"
		except:
			message = "El usuario no esta registrado"

		context = {'message':message, 'messageT':messageT}

		return render_to_response(
			'authentication/login.html',
			context,
			context_instance = RequestContext(request)
			)
class RegisterPage(TemplateView):

	def get(self,request,*args,**kwargs):
		form = GetRegister()
		generos = extraerGeneroTotales()
		context = {'form': form, 'generos':generos}
		return render(request, 'authentication/register.html', context) 

	def post(self,request,*args,**kwargs):
		form = GetRegister(request.POST)
		message=""
		messageB = True
		if form.is_valid():
			cd = form.cleaned_data 
			email = cd['email']
			name = cd['nombre']
			contrasena1 = cd['contrasena1']
			contrasena2 = cd['contrasena2']
			generos = cd['option']
			
			if(contrasena2 == contrasena1):
				try:
					usuario_p = Usuario.objects.get(email=email)
					message = "El correo ya se a registrado anteriormente."
					
				except:
					usuario = Usuario(
						email= email,
						nombre= name,
						contrasena= contrasena1,
						tipo = "Cliente",
						)
					
					usuario.save()
					for item in generos:
						genero_p = Genero.objects.get(nombre=item)
						usuario.generos.add(genero_p)
					message = "El usuario registrado con exito. Ahora inicie sesión"
					context = {'messageB':messageB, 'message':message}
					return render_to_response(
					'authentication/login.html',
					context,
					context_instance=RequestContext(request))
			else:	
				message = "Las contraseñas no coinciden."
			
		generos = extraerGeneroTotales()
		message = "Debe llenar todos los campos"
		context = { 'form':form, 'message':message, 'messageB':messageB, 'generos':generos}
		return render_to_response(
			'authentication/register.html',
			context,
			context_instance=RequestContext(request))

class Index(TemplateView):
	def get(self, request, *args, **kwargs):
		return render_to_response(
			'authentication/index.html',
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		return render_to_response(
			'authentication/login.html',
			context_instance=RequestContext(request))

class LoadGenero(TemplateView):

	def get(self,request,*args,**kwargs):
		extraerGeneroTotalesBD()
		return render_to_response(
			'authentication/generos.html', 
			context_instance=RequestContext(request))
