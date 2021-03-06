# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import models
from applications.users.models import *
from applications.movies.models import *
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
import tmdbsimple as tmdb
import sys
from numpy import *
from django.contrib import messages
from datetime import datetime
#Cambiar por el directorio en el que se encuentre el archivo clasePelicula

#Definicion de la key
tmdb.API_KEY = 'ce6b4a15c201b1ccc831cf754f9579cc'

class PeliculaAPI:

	def __init__(self, id, titulo, imagen, descripcion, fecha_estreno,trailer,reviews,generos):
		self.id = id
		self.titulo = titulo
		self.imagen = imagen
		self.descripcion = descripcion
		self.fecha_estreno = fecha_estreno
		self.trailer = trailer
		self.reviews = reviews
		self.generos = generos

def crearPeliculaBD(json, tipo):
	
	id = str(json['id'])	
	imagenJson = str(json['poster_path'])
	imagen1 = 'http://image.tmdb.org/t/p/w342' + imagenJson

	
	pelicula = Pelicula(
		codigo = str(id),
		titulo = json['title'],
		imagen = imagen1,
		descripcion = json['overview'],
		trailer = extraerTrailer(id),
		fechaEstreno = str(json['release_date']),
		)
	pelicula.save()
	extraerReviewsBD(id, pelicula)
	extraerGeneroBD(json['genre_ids'], pelicula)
	tipo_p = Tipo.objects.get(nombre=tipo)
	pelicula.tipos.add(tipo_p)

	return pelicula
	

def extraerReviewsBD(id, pelicula):
	movie = tmdb.Movies(id)
	criticas = movie.reviews(language='es')
	#print(criticas)

	if criticas['total_results'] != 0:
		#Primer campo autor, segundo contenido
		for n in movie.results:
			try:
				critica = Critica_calificacion.objects.get(critico = n['author'], critica_calificacion = n['content'])

			except:
				critica = Critica_calificacion(
				 critico = n['author'],
				 critica_calificacion = n['content'],
				 )

				critica.save()
			pelicula.criticas.add(critica)

def extraerGeneroBD(genres, pelicula):
	if len(genres) != 0:

		objGenero = tmdb.Genres()
		lista = objGenero.list(language='es')

		for n in genres:
			for f in objGenero.genres:
				if f['id'] == n:
					genero = Genero.objects.get(id_genero= f['id'])
					pelicula.generos.add(genero)


def extraerTrailer(id):
	movie = tmdb.Movies(id)
	videitos = movie.videos()
	n = movie.results
	link = 'https://www.youtube.com/watch?v='
	if len(n) != 0:
		finalLink = n[0]['key']		
		linkDefinitivo = link + finalLink

		return linkDefinitivo

	return link


def consultarTendencia(x):
	numPelis = x

	movie = tmdb.Movies()
	tendencia = movie.popular(language='es')
	tipo_p = Tipo.objects.get(nombre="Tendencia")
	for n in movie.results:

		if numPelis < 1:
			break
		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			crearPeliculaBD(n, "Tendencia")

def consultarEnCartelera(x):
	tipo_p = Tipo.objects.get(nombre="Cartelera")
	movie = tmdb.Movies()
	estreno = movie.now_playing(language='es')

	for n in movie.results:

		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			crearPeliculaBD(n, "Cartelera")


def consultarEstrenos():
	tipo_p = Tipo.objects.get(nombre="Estrenos")
	movie = tmdb.Movies()
	estreno = movie.upcoming(language='es')
	
	for n in movie.results:
		try:
			pelicula_p = Pelicula.objects.get(codigo=n)
			pelicula_p.tipos.add(tipo_p)
		except:
			pelicula = crearPeliculaBD(n, "Estrenos")


def listasPeliculas():
	listas = []	
	tendencias = [0]*4
	for i in range(4):		
		tendencias[i] = Pelicula.objects.filter(tipos="Tendencia")[i]
	ten = {'nombre':"Tendencias", 'lista':tendencias}
	listas.append(ten)	

	cartelera = [0]*4
	for i in range(4):		
		cartelera[i] = Pelicula.objects.filter(tipos="Cartelera")[i]
	ten2 = {'nombre':"En Cartelera", 'lista':cartelera}
	listas.append(ten2)

	estrenos = [0]*4
	for i in range(4):		
		estrenos[i] = Pelicula.objects.filter(tipos="Estrenos")[i]
	ten3 = {'nombre':"Estrenos", 'lista':estrenos}
	listas.append(ten3)

	return listas

def consultaPorTitulo(titulo):

	search = tmdb.Search()
	response = search.movie(query=titulo, language='es')
	peliculasTitulo= []

	if search.total_results != 0:

		for n in search.results:
			print n
			try:
				pelicula_p = Pelicula.objects.get(codigo=n)
				peliculasTitulo.append(pelicula_p)
			except:
					peliculasTitulo.append(crearPeliculaBD(n, "Regular"))

	return peliculasTitulo

def consultaPorGenero(genero, z):

	peliculasGenero = []
	generos= tmdb.Genres(genero)
	print generos
	response = generos.movies(language='es')

	if generos.total_results != 0:

		for n in generos.results:
			if z < 1:
				break
			try:
				pelicula_p = Pelicula.objects.get(codigo=n)				
				peliculasGenero.append(pelicula_p)
			except:
				peliculasGenero.append(crearPeliculaBD(n, "Regular"))
			z = z-1				

	return peliculasGenero

def consultaSimilares(pelicula, z):

	peliculas = []
	pelis= tmdb.Movies(pelicula)
	response = pelis.similar_movies(language='es')

	if pelis.total_results != 0:

		for n in pelis.results:
			if z < 1:
				break
			try:
				pelicula_p = Pelicula.objects.get(codigo=n)				
				peliculas.append(pelicula_p)
			except:
				peliculas.append(crearPeliculaBD(n, "Regular"))
			z = z-1				

	return peliculas

def consultaPorActor(actor):

	peliculasActor = []

	search = tmdb.Search()
	response = search.person(query=actor, language='es')
	
	if search.total_results != 0:

		known = search.results[0]
		knownf = known['known_for']

		print(knownf)

		if len(knownf) != 0:

			for x in knownf:
				try:
					pelicula = Pelicula.objects.get(codigo=x)
					peliculasActor.append(pelicula)
				except:
					if x['media_type'] == 'movie':
						peliculasActor.append(crearPeliculaBD(x, "Regular"))

	return peliculasActor

def calificacion(codigo, email, valor):
	calificacion = Calificacion(
		codigo = codigo,
		email = email,
		valor = valor,
		)
	calificacion.save()

#Templates-------------------------------------------------------------------------------------------------
class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class TendenciaCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarTendencia(90)
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class CarteleraCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarEnCartelera(90)
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class EstrenosCargar(TemplateView):
	def get(self,request,*args, **kwargs):
		consultarEstrenos()
		return render_to_response(
			'movies/tendencias.html',
			context_instance=RequestContext(request))

class Inicio(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = listasPeliculas()
		nombre = request.session['emailUser']
		authentication = True
		user = Usuario.objects.get(email=nombre)
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Tendencias(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		tendencias = Pelicula.objects.filter(tipos="Tendencia")
		ten = {'nombre':"Tendencias", 'lista':tendencias}
		listas.append(ten)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Cartelera(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		cartelera = Pelicula.objects.filter(tipos="Cartelera")
		ten = {'nombre':"En Cartelera", 'lista':cartelera}
		listas.append(ten)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class Estrenos(TemplateView):
	def get(self,request,*args, **kwargs):
		listas = []
		estrenos = Pelicula.objects.filter(tipos="Estrenos")
		ten = {'nombre':"Estrenos", 'lista':estrenos}
		listas.append(ten)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class ListarPorVer(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']

		user = Usuario.objects.get(email=nombre)
		listas = []
		peliculas_por_ver =[]
		porver = user.get_porver()
		codigos = porver.split(",")
		try:
			for i in codigos:
				pelicula = Pelicula.objects.get(codigo=i)
				peliculas_por_ver.append(pelicula)

		except:
				messages.info(request,"No hay peliculas por ver")

		ten = {'nombre':"Peliculas por Ver", 'lista':peliculas_por_ver}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		nombreUsuario = request.POST['usuario']
		user = Usuario.objects.get(email=nombreUsuario)
		user1 = Usuario.objects.get(email=nombre)
		listas = []
		peliculas_por_ver =[]
		porver = user.get_porver()
		codigos = porver.split(",")
		try:
			for i in codigos:
				pelicula = Pelicula.objects.get(codigo=i)
				peliculas_por_ver.append(pelicula)
			
		except:
				messages.info(request,"No hay peliculas por ver")

		ten = {'nombre':"Peliculas por Ver", 'lista':peliculas_por_ver}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user1}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class ListarVistas(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		listas = []
		peliculas_vistas =[]
		vistas = user.get_vistas()
		codigos = vistas.split(",")
		try:
			for i in codigos:			
				pelicula = Pelicula.objects.get(codigo=i)
				peliculas_vistas.append(pelicula)					
			
		except:
			messages.info(request,"No hay peliculas vistas")

		ten = {'nombre':"Peliculas Vistas", 'lista':peliculas_vistas}
		listas.append(ten)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))		
					

class VerMas(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		col = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		pelicula = Pelicula.objects.get(codigo=args[0])			
		try:
			porver = user.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False
		except:
			pass
		try:
			calificacion = Calificacion.objects.get(email=user,codigo=pelicula)
			cal= str(calificacion.valor_Calificacion) + "Estrellas"
		except:
			cal="no ha sido calificado"
		try:
			vistas1 = user.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False				
		except:
			pass

		try:
			coleccion = Coleccion.objects.get(email=user)
			coleccion_peliculas = coleccion.get_contenido()
			codigos = coleccion_peliculas.split(",")
			for i in codigos:
				if i == pelicula.codigo:
					col = False
		except:
			pass

		cines = Cine.objects.all()
		
		authentication = True
		context={'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'listasPersonalizadas': listasPersonalizadas, 'user':user}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))



	
class AgregarPorVer(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = False
		vista = True
		col=True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		try:
			pelicula = Pelicula.objects.get(codigo=args[0])

			try:
				porver = usuario.get_porver()
				tipos2 = porver.split(",")
				for i in tipos2:
					if i == pelicula.codigo:
						ver = False
			except:
				pass
			try:
				calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
				cal=str(calificacion.valor_Calificacion) + "Estrellas"
			except:
				cal="no ha sido calificado"
			try:
				vistas1 = usuario.get_vistas()
				tipos1 = vistas1.split(",")
				for i in tipos1:
					if i == pelicula.codigo:
						vista = False				
			except:
				pass

			try:
				coleccion = Coleccion.objects.get(email=usuario)
				coleccion_peliculas = coleccion.get_contenido()
				codigos = coleccion_peliculas.split(",")
				for i in codigos:
					if i == pelicula.codigo:
						col = False
			except:
				pass

			try:
				
				try:
					usuario.lista_peliculas_porver.get(codigo=pelicula.codigo)
					messages.info(request,"la pelicula ya esta en esta lista")
				except:
					usuario.lista_peliculas_porver.add(pelicula)
					messages.info(request,"la pelicula fue agregada con exito")

			except:
				ver=False

		except:
			pelicula = None

		cines = Cine.objects.all()
		authentication = True
		context={'listasPersonalizadas': listasPersonalizadas,'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

class AgregarVistas(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)		
		ver = True
		vista = False		
		col = True						
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		pelicula = Pelicula.objects.get(codigo=args[0])
					
		try:
			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False
		except:
			pass
		
		calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
		cal=str(calificacion.valor_Calificacion) + "Estrellas"
		try:
			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False				
		except:
			pass

		try:
			coleccion = Coleccion.objects.get(email=usuario)
			coleccion_peliculas = coleccion.get_contenido()
			codigos = coleccion_peliculas.split(",")
			for i in codigos:
				if i == pelicula.codigo:
					col = False
		except:
			pass

		cines = Cine.objects.all()
		authentication = True
		context={'listasPersonalizadas': listasPersonalizadas,'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))
	def post(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)		
		ver = True
		vista = False		
		col = True
		lista = request.POST['lista']
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)				
		
		pelicula = Pelicula.objects.get(codigo=args[0])
		cine = Cine.objects.get(nombre=lista)
					
		try:
			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False
		except:
			pass
		try:
			calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
			cal=str(calificacion.valor_Calificacion) + "Estrellas"
		except:
			cal="no ha sido calificado"
		try:
			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False				
		except:
			pass

		try:
			coleccion = Coleccion.objects.get(email=usuario)
			coleccion_peliculas = coleccion.get_contenido()
			codigos = coleccion_peliculas.split(",")
			for i in codigos:
				if i == pelicula.codigo:
					col = False
		except:
			pass

		try:
			
			try:
				usuario.lista_peliculas_vistas.get(codigo=pelicula.codigo)
				messages.info(request,"la pelicula ya esta en esta lista")
			except:
				try:
					usuario.lista_peliculas_vistas.add(pelicula)
										
					fecha = datetime.now()
					print fecha					
					fechaVista = FechaPeliculaVista(
						codigo = pelicula,
						email = usuario,
						fecha = fecha,
						)
					fechaVista.save()

					vi = CineVista(
						codigo=pelicula,
						email=usuario,
						cine = cine)
					vi.save()
					
					messages.info(request,"la pelicula fue agregada con exito")
				except:
					messages.info(request,"debe seleccionar un cine")					
		
				if not ver:
					usuario.lista_peliculas_porver.remove(pelicula)
					ver = True
				

		except:
			vista=False

		cines = Cine.objects.all()
		authentication = True
		context={'listasPersonalizadas': listasPersonalizadas,'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))
    
class Calificar(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)		
		ver = True
		vista = True
		col = True						
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		pelicula = Pelicula.objects.get(codigo=args[0])
					
		try:
			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False
		except:
			pass
		try:
			calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
			cal=str(calificacion.valor_Calificacion) + "Estrellas"
		except:
			cal="no ha sido calificado"
		try:
			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False				
		except:
			pass

		try:
			coleccion = Coleccion.objects.get(email=usuario)
			coleccion_peliculas = coleccion.get_contenido()
			codigos = coleccion_peliculas.split(",")
			for i in codigos:
				if i == pelicula.codigo:
					col = False
		except:
			pass

		cines = Cine.objects.all()
		authentication = True
		context={'listasPersonalizadas': listasPersonalizadas,'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))
	def post(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)		
		ver = True
		vista = True		
		col = True
		ca= request.POST['calificacion']	
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)					
		
		pelicula = Pelicula.objects.get(codigo=args[0])
		try:
			usuario.lista_peliculas_vistas.get(codigo=pelicula.codigo)
			try:

				calificacion = Calificacion(
					email=usuario,
					codigo=pelicula,
					valor_Calificacion=ca,
					)	
				calificacion.save()

			except:
				calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
				calificacion.valor_Calificacion=ca
				calificacion.save()
			messages.info(request,"La pelicula fue calificada")
		except:
			messages.info(request,"debe haber visto la pelicula")
		try:
			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False
		except:
			pass
		try:
			calificacion = Calificacion.objects.get(email=usuario,codigo=pelicula)
			cal=str(calificacion.valor_Calificacion) + " Estrellas"
		except:
			cal="no ha sido calificado"
		try:
			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False				
		except:
			pass

		try:
			coleccion = Coleccion.objects.get(email=user)
			coleccion_peliculas = coleccion.get_contenido()
			codigos = coleccion_peliculas.split(",")
			for i in codigos:
				if i == pelicula.codigo:
					col = False
		except:
			pass



		cines = Cine.objects.all()
		authentication = True
		context={'listasPersonalizadas': listasPersonalizadas,'cal':cal,'cines':cines,'col':col,'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))
    

class Busqueda(TemplateView):
	def post(self,request,*args, **kwargs):
		busqueda = request.POST['busqueda']
		tipo = request.POST['tipo']
		if(busqueda != ""):
			nombre = request.session['emailUser']
			user = Usuario.objects.get(email=nombre)
			authentication = True
			listas = []
			print tipo
			if tipo == "titulo":
				lista = consultaPorTitulo(busqueda)
				nombre_q = "Resultados busqueda por titulo de: " + busqueda				
				busqueda = {'nombre':nombre_q, 'lista':lista}
				listas.append(busqueda)
			elif tipo == "actor":
				lista = consultaPorActor(busqueda)
				nombre_q = "Resultados busqueda por actor de: " + busqueda
				
				busqueda = {'nombre':nombre_q, 'lista':lista}
				listas.append(busqueda)

			context={'authentication':authentication, 'nombre':nombre, 'listas':listas}
			return render_to_response(
				'movies/inicio.html',
				context,
				context_instance=RequestContext(request))
		else:
			nombre = request.session['emailUser']
			authentication = True
			context={'authentication':authentication, 'nombre':nombre, 'user':user}
			return render_to_response(
				'movies/inicio.html',
				context,
				context_instance=RequestContext(request))


class Prueba(TemplateView):
	def get(self,request,*args, **kwargs):
		lol = "r"
		l = "apsito"
		pelicula = Usuario(
			email="dhurvrfb",
			nombre="mateo",
			contrasena="1234567",
			tipo="admin"
			)
		pelicula.save()

		context = {'lol':lol, 'l':l, 'pelicula':pelicula}
		return render_to_response(

			'movies/movie.html',context,
			context_instance=RequestContext(request))

class Index(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'user':user}
		return render_to_response(

			'movies/inicio.html',context,
			context_instance=RequestContext(request))

