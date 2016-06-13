# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import Prueba
from .views import Index
from .views import TendenciaCargar
from .views import CarteleraCargar
from .views import EstrenosCargar
from .views import Inicio
from .views import Tendencias
from .views import Cartelera
from .views import Estrenos 
from .views import VerMas
from .views import Busqueda


urlpatterns = [
	url(r'^tendenciasCargar/$', TendenciaCargar.as_view(), name='tendenciaCargar'),
	url(r'^carteleraCargar/$', CarteleraCargar.as_view(), name='carteleraCargar'),
	url(r'^estrenosCargar/$', EstrenosCargar.as_view(), name='estrenosCargar'),
    url(r'^movies/movie/$', Prueba.as_view(), name='prueba'),
    url(r'^movies/index/$', Index.as_view(), name='index'),
    url(r'^movies/inicio/$', Inicio.as_view(), name='inicio'),
    url(r'^movies/tendencias/$', Tendencias.as_view(), name='tendencias'),
    url(r'^movies/cartelera/$', Cartelera.as_view(), name='cartelera'),
    url(r'^movies/estrenos/$', Estrenos.as_view(), name='estrenos'),
    url(r'^movies/verMas/(\d+)$', VerMas.as_view(), name='verMas'),
    url(r'^movies/busqueda/$', Busqueda.as_view(), name='busqueda'),

]