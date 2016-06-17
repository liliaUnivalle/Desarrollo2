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

# Create your views here.

class IndexView(TemplateView):
	def get(self,request,*args, **kwargs):
		
		return render_to_response(
			'users/login.html',
			context_instance=RequestContext(request))


class Perfil(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		nombre2 = request.session['nombre']
		authentication = True
		listasPersonalizadas =  Lista_personal.objects.all()
		context={'authentication':authentication, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas }
		return render_to_response(
			'users/perfil.html',
			context,
			context_instance=RequestContext(request))

class CrearNuevaLista(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		nombre2 = request.session['nombre']
		authentication = True
		valor = request.POST['nombreLista']
		user = Usuario.objects.get(email=nombre)
		try:
			lista = Lista_personal.objects.get(nombre=valor, email=user)
		except:
			listaCreada = Lista_personal(
				nombre=valor,
				email=user,
				)
			listaCreada.save()

		listasPersonalizadas =  Lista_personal.objects.all()
		context={'authentication':authentication, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas }
		return render_to_response(
			'users/perfil.html',
			context,
			context_instance=RequestContext(request))