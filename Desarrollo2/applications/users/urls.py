# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import IndexView
from .views import Perfil
from .views import CrearNuevaLista
from .views import ListarListaPersonal
from .views import AgregarAListaPersonal

urlpatterns = [
	url(r'^users/perfil/$', Perfil.as_view(), name='perfil'),
	url(r'^users/nuevaLista/$', CrearNuevaLista.as_view(), name='nuevaLista'),
	url(r'^users/listarListaPersonal/$', ListarListaPersonal.as_view(), name='listarListaPersonal'),   
    url(r'^users/agregarAListaPersonal/(\d+)$', AgregarAListaPersonal.as_view(), name='agregarAListaPersonal'), 
    
]