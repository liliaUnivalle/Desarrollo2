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
# Create your views here.

class LoginPage(TemplateView):

	def get(self,request,*args,**kwargs):
		return render_to_response(
			'authentication/login.html',
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		username = request.POST['username']
		password = request.POST['password']

		#user = authenticate(username=username, password=password)
		message = ""
		if user is not None:
			# the password verified for the user
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('movies:movie'))
			else:
				message = "La contraseña es invalida, o el usuario esta inactivo"
		else:
			# the authentication system was unable to verify the username and password
			message = "El usuario o la contraseña son incorrectos"

		context = {'message':message}

		return render_to_response(
			'authentication/login.html',
			context,
			context_instance = RequestContext(request)
			)
class RegisterPage(TemplateView):

	def get(self,request,*args,**kwargs):
		return render_to_response('authentication/register.html')