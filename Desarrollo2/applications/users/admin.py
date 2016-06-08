from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
	list_display = (
		'email','nombre','contrasena','tipo','get_generos'
		)

	search_fields = ()
admin.site.register(Usuario, UsuarioAdmin)

class Lista_peliculas_porverAdmin(admin.ModelAdmin):
	list_display = (
		'email','codigo'
		)

	search_fields = ()
admin.site.register(Lista_peliculas_porver,Lista_peliculas_porverAdmin)

class Lista_peliculas_vistasAdmin(admin.ModelAdmin):
	list_display = (
		'email','codigo','fecha'
		)

	search_fields = ()
admin.site.register(Lista_peliculas_vistas, Lista_peliculas_vistasAdmin)

class Lista_personalAdmin(admin.ModelAdmin):
	list_display = (
		'nombre','email'
		)

	search_fields = ()
admin.site.register(Lista_personal, Lista_personalAdmin)

class ColeccionlAdmin(admin.ModelAdmin):
	list_display = (
		'genero','email'
		)

	search_fields = ()
admin.site.register(Coleccion, ColeccionlAdmin)
class ContieneColeccionAdmin(admin.ModelAdmin):
	list_display = (
		'genero','email','codigo'
		)

	search_fields = ()
admin.site.register(ContieneColeccion, ContieneColeccionAdmin)

class ContieneAdmin(admin.ModelAdmin):
	list_display = (
		'nombre','email','codigo'
		)

	search_fields = ()
admin.site.register(Contiene, ContieneAdmin)

class CalificaAdmin(admin.ModelAdmin):
	list_display = (
		'codigo','email','valor_Calificacion'
		)

	search_fields = ()
admin.site.register(Califica, CalificaAdmin)
# Register your models here.
