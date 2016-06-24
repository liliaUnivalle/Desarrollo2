from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
	list_display = (
		'email','nombre','contrasena','tipo','get_generos', 'get_vistas', 'get_porver'
		)

	search_fields = ()
admin.site.register(Usuario, UsuarioAdmin)



class Lista_personalAdmin(admin.ModelAdmin):
	list_display = (
		'nombre','email','get_contenido'
		)

	search_fields = ()
admin.site.register(Lista_personal, Lista_personalAdmin)

class ColeccionlAdmin(admin.ModelAdmin):
	list_display = (
		'id_genero','email','get_contenido'
		)

	search_fields = ()
admin.site.register(Coleccion, ColeccionlAdmin)


class CalificaAdmin(admin.ModelAdmin):
	list_display = (
		'get_pelicula','get_email','valor_Calificacion'
		)

	search_fields = ()
admin.site.register(Calificacion, CalificaAdmin)

class FechaAdmin(admin.ModelAdmin):
	list_display = (
		'get_pelicula','get_email','fecha'
		)

	search_fields = ()
admin.site.register(FechaPeliculaVista, FechaAdmin)


# Register your models here.
