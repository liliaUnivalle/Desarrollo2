from django.contrib import admin
from .models import *

class PeliculaAdmin(admin.ModelAdmin):
	list_display = (
		'codigo',
		)

	search_fields = ()
admin.site.register(Pelicula, PeliculaAdmin)

class GeneroAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		)

	search_fields = ()
admin.site.register(Genero, GeneroAdmin)

class Critica_calificacionAdmin(admin.ModelAdmin):
	list_display = (
		'codigo','Critica_calificacion','critico'
		)

	search_fields = ()
admin.site.register(Critica_calificacion, Critica_calificacionAdmin)
# Register your models here.
