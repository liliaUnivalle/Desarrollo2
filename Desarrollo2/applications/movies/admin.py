from django.contrib import admin
from .models import *

class PeliculaAdmin(admin.ModelAdmin):
	list_display = (
		'codigo','titulo','imagen','descripcion','trailer','fechaEstreno','get_criticas','get_generos','get_tipos', 'get_actores'
		)

	search_fields = ()
admin.site.register(Pelicula, PeliculaAdmin)


class Critica_calificacionAdmin(admin.ModelAdmin):
	list_display = (
		'critica_calificacion','critico'
		)

	search_fields = ()
admin.site.register(Critica_calificacion, Critica_calificacionAdmin)


class GeneroAdmin(admin.ModelAdmin):
	list_display = (
		'id_genero','nombre'
		)

	search_fields = ()
admin.site.register(Genero, GeneroAdmin)

class TipoAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		)

	search_fields = ()
admin.site.register(Tipo, TipoAdmin)

class ActorAdmin(admin.ModelAdmin):
	list_display = (
		'nombre',
		)

	search_fields = ()
admin.site.register(Actor, ActorAdmin)
# Register your models here.
