# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import IndexView
from .views import Cliente
from .views import CrearNuevaLista
from .views import ListarListaPersonal
from .views import AgregarAListaPersonal
from .views import Admin
from .views import AdminAuditor

urlpatterns = [
	url(r'^users/cliente/$', Cliente.as_view(), name='perfil'),
	url(r'^users/nuevaLista/$', CrearNuevaLista.as_view(), name='nuevaLista'),
	url(r'^users/listarListaPersonal/$', ListarListaPersonal.as_view(), name='listarListaPersonal'),   
    url(r'^users/agregarAListaPersonal/(\d+)$', AgregarAListaPersonal.as_view(), name='agregarAListaPersonal'), 
    url(r'^users/admin$', Admin.as_view(), name='admin'),
    url(r'^users/adminAuditor$', AdminAuditor.as_view(), name='adminAuditor'),   
]