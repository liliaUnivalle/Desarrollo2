# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import LoginPage
from .views import RegisterPage

urlpatterns = [
    url('^$', LoginPage.as_view(), name='login'),
    url(r'^register/$', RegisterPage.as_view(), name='register'),
 ]