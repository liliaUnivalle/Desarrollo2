from django.contrib import admin
from .models import Pelicula
from .models import Critica_calificacion

class PeliculaAdmin(admin.ModelAdmin):
	list_display = (
		'codigo',
		)

	search_fields = ()
admin.site.register(Pelicula, PeliculaAdmin)

class Critica_calificacionAdmin(admin.ModelAdmin):
	list_display = (
		'codigo','Critica_calificacion','critico'
		)

	search_fields = ()
admin.site.register(Critica_calificacion, Critica_calificacionAdmin)
# Register your models here.
