# -*- encoding: utf-8 -*-

from django import forms


class GetRegister(forms.Form):

	email = forms.EmailField()
	nombre = forms.CharField()
	contrasena1 = forms.CharField()
	contrasena2 = forms.CharField()