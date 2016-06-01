# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import IndexView
from .views import Prueba

urlpatterns = [
    url(r'^movies/movie/$', Prueba.as_view(), name='index'),
    url('^$', IndexView.as_view(), name='prueba'),
]