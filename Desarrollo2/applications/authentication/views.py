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

class LoginPage(TemplateView):

	def get(self,request,*args,**kwargs):
		
		return render_to_response(
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
		return render(request, 'authentication/register.html', {'form': form}) 

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
			if(contrasena2 == contrasena1):
				try:
					usuario_p = Usuario.objects.get(email=email)
					message = "El correo ya se a registrado anteriormente."
					
				except:
					usuario = Usuario(
						email= email,
						nombre= name,
						contrasena= contrasena1,
						)
					
					usuario.save()
					message = "El usuario registrado con exito. Ahora inicie sesión"
					context = {'messageB':messageB, 'message':message}
					return render_to_response(
					'authentication/login.html',
					context,
					context_instance=RequestContext(request))
			else:	
				message = "Las contraseñas no coinciden."
				

		message = "Debe llenar todos los campos"
		context = { 'form':form, 'message':message, 'messageB':messageB}
		return render_to_response(
			'authentication/register.html',
			context,
			context_instance=RequestContext(request))