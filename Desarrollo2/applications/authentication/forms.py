# -*- encoding: utf-8 -*-

from django import forms



class GetRegister(forms.Form):

	email = forms.EmailField()
	nombre = forms.CharField()
	contrasena1 = forms.CharField()
	contrasena2 = forms.CharField()
	option = forms.MultipleChoiceField(		
        choices= (("Documental","Documental"),
        	("Misterio","Misterio"),
        	("Ciencia ficción", "Ciencia ficción"),
        	("Crimen", "Crimen"),
        	("Suspense", "Suspense"),
        	("Western","Western"),
        	("Historia","Historia"),
        	("Comedia","Comedia"),
        	("Acción","Acción"),
        	("Terror","Terror"),
        	("Drama","Drama"),
        	("Animación","Animación"),
        	("Fantasía","Fantasía"),
        	("Aventura","Aventura"),
        	("película de la televisión","película de la televisión"),
        	("Foreign","Foreign"),
        	("Guerra","Guerra"),
        	("Familia","Familia"),
        	("Romance","Romance"),
        	("Música","Música"),
        ), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

