# -*- encoding: utf-8 -*-

from django import forms

import tmdbsimple as tmdb
import sys
from numpy import *
#Cambiar por el directorio en el que se encuentre el archivo clasePelicula
sys.path.append('./Desktop')
from applications.movies.views import Pelicula

tmdb.API_KEY = 'ce6b4a15c201b1ccc831cf754f9579cc'

def extraerGeneroTotales2():	

	generos = []
	objGenero = tmdb.Genres()
	lista = objGenero.list()
	generosInfo = lista[u'genres']
	for i in generosInfo:
		lista=[]
		lista.append(i[u'name'])
		lista.append(i[u'name'])
		generos.append(lista)
	return generos

def extraerGeneroTotales():	

	generos = []
	objGenero = tmdb.Genres()
	lista = objGenero.list()
	generosInfo = lista[u'genres']
	for i in generosInfo:
		generos.append(i[u'name'])
	return generos

generos = extraerGeneroTotales2()

class GetRegister(forms.Form):

	email = forms.EmailField()
	nombre = forms.CharField()
	contrasena1 = forms.CharField()
	contrasena2 = forms.CharField()
	option = forms.ModelMultipleChoiceField(		
        queryset = (("Action","Action"),
        	("Adventure","Adventure"),
        	("Animation", "Animation"),
        	("Comedy", "Comedy"),
        	("Crime", "Crime"),
        	("Documentary","Documentary"),
        	("Drama","Drama"),
        	("Family","Family"),
        	("Fantasy","Fantasy"),
        	("Foreing","Foreing"),
        	("History","History"),
        	("Horror","Horror"),
        	("Music","Music"),
        	("Mistery","Mistery"),
        	("Romance","Romance"),
        	("Science Fiction","Science Fiction"),
        	("TV Movie","TV Movie"),
        	("Thriler","Thriler"),
        	("War","War"),
        	("Western","Western"),
        ), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

"""
( None, ("Action","Action"),
        	("Adventure","Adventure"),
        	("Animation", "Animation"),
        	("Comedy", "Comedy"),
        	("Crime", "Crime"),
        	("Documentary","Documentary"),
        	("Drama","Drama"),
        	("Family","Family"),
        	("Fantasy","Fantasy"),
        	("Foreing","Foreing"),
        	("History","History"),
        	("Horror","Horror"),
        	("Music","Music"),
        	("Mistery","Mistery"),
        	("Romance","Romance"),
        	("Science Fiction","Science Fiction"),
        	("TV Movie","TV Movie"),
        	("Thriler","Thriler"),
        	("War","War"),
        	("Western","Western"),
        )
"""