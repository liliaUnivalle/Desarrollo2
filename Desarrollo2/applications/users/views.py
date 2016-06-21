# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import models 
from django.shortcuts import render
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
from .models import *
from django.contrib import messages
from applications.authentication.forms import GetRegister
from django.contrib import messages

# Create your views here.

class IndexView(TemplateView):
	def get(self,request,*args, **kwargs):
		
		return render_to_response(
			'users/login.html',
			context_instance=RequestContext(request))


class Cliente(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		context={'authentication':authentication, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas , 'user':user}
		return render_to_response(
			'users/cliente.html',
			context,
			context_instance=RequestContext(request))

class CrearNuevaLista(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		valor = request.POST['nombreLista']
		user = Usuario.objects.get(email=nombre)

		try:
			lista = Lista_personal.objects.get(nombre=valor, email=user)
			messages.info(request,"la lista ya existe")
		except:
			listaCreada = Lista_personal(
				nombre=valor,
				email=user,
				)
			listaCreada.save()
			messages.info(request,"la lista fue creada con exito")

		listasPersonalizadas =  Lista_personal.objects.all()
		context={'authentication':authentication, 'nombre':nombre, 'user':user, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas }
		return render_to_response(
			'users/cliente.html',
			context,
			context_instance=RequestContext(request))

class ListarListaPersonal(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		lista = request.POST['lista']
		lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	 	
		listas = []
		vistas = lista_personal. get_contenido()
		codigos = vistas.split(",")
		listaPersonal =[]
		for i in codigos:
			try:
				pelicula = Pelicula.objects.get(codigo=i)
				listaPersonal.append(pelicula)
			except:
				print "Hay error"

		ten = {'nombre':"Lista Personal: "+lista, 'lista':listaPersonal}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication, 'user':usuario, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/listaPersonal.html',
			context,
			context_instance=RequestContext(request))

class AgregarAListaPersonal(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		try:
			pelicula = Pelicula.objects.get(codigo=args[0])

			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False

			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False
		
		except:
			pelicula = None

		
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'user':usuario, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'listasPersonalizadas': listasPersonalizadas}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)

		try:
			pelicula = Pelicula.objects.get(codigo=args[0])

			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False

			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False

			lista = request.POST['lista']
			lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	 
			try:
				lista_personal.contenido.get(codigo=pelicula.codigo)
				messages.info(request,"la pelicula ya esta en esta lista")
			except:
				lista_personal.contenido.add(pelicula)
				messages.info(request,"la pelicula fue agregada con exito")

		except:
			pelicula = None		
		
		authentication = True
		context={'authentication':authentication,'user':usuario, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'listasPersonalizadas': listasPersonalizadas}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

class EliminarDeListaPersonal(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		lista =  args[0]
		codigo = args[1]
		lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	
		pelicula = Pelicula.objects.get(codigo=i)
		try:
			listaPersonal.remove(pelicula) 
			messages.info(request,"hubo error")
		except:
			messages.info(request,"Se elimino con exito")

		listas = []
		vistas = lista_personal. get_contenido()
		codigos = vistas.split(",")
		listaPersonal =[]
		for i in codigos:
			try:
				pelicula = Pelicula.objects.get(codigo=i)
				listaPersonal.append(pelicula)
			except:
				print "Hay error"

		ten = {'nombre':"Lista Personal: "+lista, 'lista':listaPersonal}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication,'user':usuario, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/listaPersonal.html',
			context,
			context_instance=RequestContext(request))

class Admin(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'nombre2':nombre2, 'user':user}
		return render_to_response(
			'users/admin.html',
			context,
			context_instance=RequestContext(request))

class AdminAuditor(TemplateView):
	def get(self,request,*args, **kwargs):
		form = GetRegister()
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre,'form':form, 'user':user}
		return render_to_response(
			'users/adminAuditor.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		form = GetRegister(request.POST)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True	
		if form.is_valid():
			cd = form.cleaned_data 
			email = cd['email']
			name = cd['nombre']
			contrasena1 = cd['contrasena1']
			contrasena2 = cd['contrasena2']			
			
			if(contrasena2 == contrasena1):
				try:
					usuario_p = Usuario.objects.get(email=email)
					message = "El correo ya se a registrado anteriormente."
					
				except:
					usuario = Usuario(
						email= email,
						nombre= name,
						contrasena= contrasena1,
						tipo = "Auditor",
						)
					
					usuario.save()
					message = "El auditor fue creado con exito. "
			else:	
				message = "Las contraseñas no coinciden."
		else:
			message = "Debe llenar todos los campos"
		
		context={'authentication':authentication, 'form':form,'nombre':nombre, 'user':user}
		return render_to_response(
		'users/adminAuditor.html',
		context,
		context_instance=RequestContext(request))