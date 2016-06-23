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
from .views import EliminarDeListaPersonal
from .views import ListarCalificaciones
from .views import ListasAdmin
from .views import Recomendaciones
from .views import ListarVistasPorGenero
from .views import ListarTodasLasPeliculas

urlpatterns = [
	url(r'^users/cliente/$', Cliente.as_view(), name='perfil'),
	url(r'^users/nuevaLista/$', CrearNuevaLista.as_view(), name='nuevaLista'),
	url(r'^users/listarListaPersonal/$', ListarListaPersonal.as_view(), name='listarListaPersonal'),   
    url(r'^users/agregarAListaPersonal/(\d+)$', AgregarAListaPersonal.as_view(), name='agregarAListaPersonal'), 
    url(r'^users/admin$', Admin.as_view(), name='admin'),
    url(r'^users/adminAuditor$', AdminAuditor.as_view(), name='adminAuditor'),  
    url(r'^users/eliminarDeListaPersonal/(\d+)$', EliminarDeListaPersonal.as_view(), name='eliminarDeListaPersonal'),
    url(r'^users/calificaciones/$', ListarCalificaciones.as_view(), name='calificaciones'),
    url(r'^users/listasAdmin/$', ListasAdmin.as_view(), name='listasAdmin'),  
    url(r'^users/recomendaciones/$', Recomendaciones.as_view(), name='recomendaciones'), 
    url(r'^users/listarVistasPorGenero/$', ListarVistasPorGenero.as_view(), name='listarVistasPorGenero'), 
    url(r'^users/listarTodasLasPelicula/$', ListarTodasLasPeliculas.as_view(), name='listarTodasLasPelicula'),
    
]