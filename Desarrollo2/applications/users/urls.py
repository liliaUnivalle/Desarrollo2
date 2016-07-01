# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import *

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
    url(r'^users/vistasUltimoMes/$', MasVistasUltimoMes.as_view(), name='vistasUltimoMes'),
    url(r'^users/generosMasVistosUltimoMes/$', GenerosMasVistosUltimoMes.as_view(), name='generosMasVistosUltimoMes'),
    url(r'^users/coleccion/$', ListarColeccion.as_view(), name='coleccion'),    
    url(r'^users/agregarColeccion/(\d+)$', AgregarColeccion.as_view(), name='agregarColeccion'),    
    url(r'^users/estadisticas$', Estadisticas.as_view(), name='estadisticas'),    
    url(r'^users/cines$', PeliculasPorCine.as_view(), name='cines'),
    url(r'^users/editar$', Editar.as_view(), name='editar'),    
]