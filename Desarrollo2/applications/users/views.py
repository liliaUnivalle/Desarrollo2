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

class IndexView(TemplateView):
	def get(self,request,*args, **kwargs):
		
		return render_to_response(
			'users/login.html',
			context_instance=RequestContext(request))