# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import Prueba
from .views import Index
from .views import Tendencia
from .views import Inicio

urlpatterns = [
    url(r'^movies/movie/$', Prueba.as_view(), name='prueba'),
    url(r'^movies/index/$', Index.as_view(), name='index'),
    url(r'^movies/inicio/$', Inicio.as_view(), name='inicio'),
    url(r'^tendencias/$', Tendencia.as_view(), name='tendencias'),
]