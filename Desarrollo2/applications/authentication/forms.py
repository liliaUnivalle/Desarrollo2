# -*- encoding: utf-8 -*-

from django import forms



class GetRegister(forms.Form):

	email = forms.EmailField()
	nombre = forms.CharField()
	contrasena1 = forms.CharField()
	contrasena2 = forms.CharField()
	option = forms.MultipleChoiceField(		
        choices= (("Action","Action"),
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

