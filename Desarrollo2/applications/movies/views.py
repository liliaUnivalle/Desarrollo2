# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

class Explorer(TemplateView):
    def get(self,request,*args,**kwargs):
    	return render_to_response(
    		'movies/explorer.html',
    		context_instance=RequestContext(request))
