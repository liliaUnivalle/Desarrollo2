# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import IndexView
from .views import Perfil
from .views import CrearNuevaLista

urlpatterns = [
	url(r'^users/perfil/$', Perfil.as_view(), name='perfil'),
	url(r'^users/nuevaLista/$', CrearNuevaLista.as_view(), name='nuevaLista'),
]