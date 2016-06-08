# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import LoginPage
from .views import RegisterPage
from .views import Index
from .views import LoadGenero

urlpatterns = [
    url('^$', Index.as_view(), name='index'),
    url(r'^login/$', LoginPage.as_view(), name='login'),
    url(r'^register/$', RegisterPage.as_view(), name='register'),
    url(r'^generos/$', LoadGenero.as_view(), name='genero'),
 ]