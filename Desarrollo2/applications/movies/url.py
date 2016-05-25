 -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import IndexView

urlpatterns = [
    url('^$', Explorer.as_view(), name='explorer'),
]