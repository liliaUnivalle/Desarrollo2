# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import models 
from django.shortcuts import render
from Desarrollo2.settings import FILES_ROOT
from Desarrollo2.settings import MEDIA_ROOT
from .models import *
from applications.movies.views import consultaPorGenero
from applications.movies.views import consultaSimilares
from django.contrib import messages
from applications.authentication.forms import GetRegister
from django.contrib import messages
from datetime import datetime
from heapq import merge

# Create your views here.

class CineClass:
	def __init__(self, nombreCine, matriz):
		self.nombreCine = nombreCine
		self.matriz = matriz

def generarRecomendaciones(nombre, user):
	peliculasVistas = user.lista_peliculas_vistas
	listas = []
	vistas = user.get_vistas()
	codigos = vistas.split(",")

	matriz = []
	generos = Genero.objects.all()
	for i in range(len(generos)):
	    matriz.append([])
	    matriz[i].append(0)
	    matriz[i].append(generos[i].id_genero)
	    

	for i in codigos:
		try:
			print i
			pelicula = Pelicula.objects.get(codigo=i)			
			for e in matriz:
				gens = pelicula.get_generos()				
				gens2 = gens.split(",")
				for s in gens2:
					if e[1] == s:
						e[0] = e[0] +1												
			
		except:
			print "hay error"


	gensU = user.get_generos()	
	gens3 = gensU.split(",")
	for e in matriz:
		for s in gens3:
			if e[1] == s:
				e[0] = e[0] +3

	matriz.sort(reverse=True)
	peliculas = []
	#for i in codigos:
	#	lista = consultaSimilares(i, 10)
	#	peliculas = list(merge(lista, peliculas))
	for i in range(3):
		lista = consultaPorGenero(matriz[i][1], 10)
		peliculas.extend([element for element in lista if element not in peliculas])
		
	return peliculas

def peliculasVistasUltimoMes():
	fecha = datetime.now()
	mes = fecha.month
	dia = fecha.day
	an_o= fecha.year

	diaAnterior = dia
	an_oAnterior = an_o

	hora = fecha.hour
	minuto = fecha.minute
	segundo = fecha.second

	if (mes > 1):
		mesAnterior = mes-1
	else:
		mesAnterior = 12
		an_oAnterior = an_o-1
	if mes == 2 and dia > 28:
		diaAnterior = 28
	if dia == 31:
		if mes == 4 and mes == 6 and mes == 9 and mes == 11:
			diaAnterior = 30

	nuevaFecha = str(diaAnterior)+"-"+str(mesAnterior)+"-"+str(an_oAnterior)+" "+str(hora)+":"+str(minuto)+":"+str(segundo) 
	fecha2 = datetime.strptime(nuevaFecha, "%d-%m-%Y %H:%M:%S")

	vistas = FechaPeliculaVista.objects.filter(fecha__gte=fecha2)
	return vistas

def peliculasMasVistasUltimoMes():
	
	vistas = peliculasVistasUltimoMes()
	matriz = []
	conf=False
	for i in range(len(vistas)):
		for e in matriz:
			if e[1].codigo == vistas[i].codigo.codigo:
				e[0] = e[0]+1
				conf = True

		if not conf:
		    matriz.append([])
		    matriz[i].append(1)
		    matriz[i].append(vistas[i].codigo)
		    conf = False

	matriz.sort(reverse=True)
	matriz2=[]
	for i in matriz:
		dic = {'cantidad':i[0], 'pelicula':i[1]}
		matriz2.append(dic)

	return matriz2

def generosMasVistosUltimoMes():
	
	vistas = peliculasVistasUltimoMes()
	matriz = []
	generos = Genero.objects.all()
	for i in range(len(generos)):
	    matriz.append([])
	    matriz[i].append(0)
	    matriz[i].append(generos[i])

	for i in vistas:
		try:
			pelicula = i.codigo	
			for e in matriz:
				gens = pelicula.get_generos()				
				gens2 = gens.split(",")
				for s in gens2:
					if e[1].id_genero == s:
						e[0] = e[0] +1
		except:
			print "hay error"				

	matriz.sort(reverse=True)
	matriz2=[]
	for i in matriz:
		if i[0] != 0:
			dic = {'cantidad':i[0], 'genero':i[1]}
			matriz2.append(dic)

	return matriz2

def numeroRegistros():
	users = Usuario.objects.filter(tipo="Cliente")
	num = len(users)
	return num

def peliculasVistas(user):
	peliculas=[]
	vistas = user.get_vistas()
	codigos = vistas.split(",")
	for i in codigos:
		try:
			pelicula = Pelicula.objects.get(codigo=i)
			peliculas.append(pelicula)
		except:
			pass

	return peliculas

def peliculasVer(user):
	peliculas=[]
	vistas = user.get_porver()
	codigos = vistas.split(",")
	for i in codigos:
		try:
			pelicula = Pelicula.objects.get(codigo=i)
			peliculas.append(pelicula)
		except:
			pass

	return peliculas


def peliculasVistasEst():
	users = Usuario.objects.filter(tipo="Cliente")
	vistas = []
	for i in users:
		lista = peliculasVistas(i)
		vistas.extend([element for element in lista if element not in vistas])
	num = len(vistas)
	return num

def peliculasPorVerEst():
	users = Usuario.objects.filter(tipo="Cliente")
	vistas = []
	for i in users:
		lista = peliculasVer(i)
		vistas.extend([element for element in lista if element not in vistas])
	num = len(vistas)
	return num

def peliculasCalificadasEst():
	users = Usuario.objects.filter(tipo="Cliente")
	lista=[]
	for i in users:
		listaM =[]
		calificaciones = Calificacion.objects.filter(email=i.email)
		for e in calificaciones:
			listaM.append(e.codigo)
		lista.extend([element for element in listaM if element not in  lista])

	num = len(lista)
	print "peliculas calificadas: "+str(num)
	return num

def peliculasEnColecciones():
	colecciones = Coleccion.objects.all()
	listaR=[]
	for i in colecciones:
		listaM=[]
		lista = i.get_contenido()
		lista2=lista.split(",")
		for e in lista2:
			print e
			try:
				pelicula = Pelicula.objects.get(codigo=e)
				listaM.append(pelicula)
			except:
				pass
		listaR.extend([element for element in listaM if element not in  listaR])
	num = len(listaR)
	return num

#----------------Templates------------------------------------------------------------------

class IndexView(TemplateView):
	def get(self,request,*args, **kwargs):
		
		return render_to_response(
			'users/login.html',
			context_instance=RequestContext(request))

class Cliente(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		generos = Genero.objects.all()
		context={'authentication':authentication, 'generos':generos, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas , 'user':user}
		return render_to_response(
			'users/cliente.html',
			context,
			context_instance=RequestContext(request))

class CrearNuevaLista(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		valor = request.POST['nombreLista']
		user = Usuario.objects.get(email=nombre)

		try:
			lista = Lista_personal.objects.get(nombre=valor, email=user)
			messages.info(request,"la lista ya existe")
		except:
			listaCreada = Lista_personal(
				nombre=valor,
				email=user,
				)
			listaCreada.save()
			messages.info(request,"la lista fue creada con exito")

		listasPersonalizadas =  Lista_personal.objects.all()
		context={'authentication':authentication, 'nombre':nombre, 'user':user, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas }
		return render_to_response(
			'users/listasCliente.html',
			context,
			context_instance=RequestContext(request))

class ListarListaPersonal(TemplateView):
	def get(self,request,*args, **kwargs):		
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		lista =request.session['lista'] 	
		lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	 	
		listas = []
		vistas = lista_personal. get_contenido()
		codigos = vistas.split(",")
		listaPersonal =[]
		for i in codigos:
			try:
				pelicula = Pelicula.objects.get(codigo=i)
				listaPersonal.append(pelicula)
			except:
				print "Hay error"

		ten = {'nombre':"Lista Personal: "+lista, 'lista':listaPersonal}
		listas.append(ten)
		tam = len(listaPersonal)
		if tam == 0:
			messages.info(request,"la lista está vacía")
		authentication = True
		context={'authentication':authentication, 'user':usuario, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/listaPersonal.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args, **kwargs):		
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		lista = request.POST['lista']
		request.session['lista'] = lista	
		if lista == "--":		
			nombre2 = request.session['nombre']
			authentication = True
			listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
			generos = Genero.objects.all()
			messages.info(request,"debe seleccionar una lista")
			context={'authentication':authentication, 'generos':generos, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas , 'user':usuario}
			return render_to_response(
				'users/cliente.html',
				context,
				context_instance=RequestContext(request))
		else:
			lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	 	
			listas = []
			vistas = lista_personal. get_contenido()
			codigos = vistas.split(",")
			listaPersonal =[]
			for i in codigos:
				try:
					pelicula = Pelicula.objects.get(codigo=i)
					listaPersonal.append(pelicula)
				except:
					print "Hay error"

			ten = {'nombre':"Lista Personal: "+lista, 'lista':listaPersonal}
			listas.append(ten)
			tam = len(listaPersonal)
			if tam == 0:
				messages.info(request,"la lista está vacía")
			authentication = True
			context={'authentication':authentication, 'user':usuario, 'nombre':nombre, 'listas':listas}
			return render_to_response(
				'movies/listaPersonal.html',
				context,
				context_instance=RequestContext(request))

class AgregarAListaPersonal(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		try:
			pelicula = Pelicula.objects.get(codigo=args[0])

			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False

			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False
		
		except:
			pelicula = None

		cines = Cine.objects.all()
		authentication = True
		context={'cines':cines,'authentication':authentication, 'nombre':nombre, 'user':usuario, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'listasPersonalizadas': listasPersonalizadas}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)

		try:
			pelicula = Pelicula.objects.get(codigo=args[0])

			porver = usuario.get_porver()
			tipos2 = porver.split(",")
			for i in tipos2:
				if i == pelicula.codigo:
					ver = False

			vistas1 = usuario.get_vistas()
			tipos1 = vistas1.split(",")
			for i in tipos1:
				if i == pelicula.codigo:
					vista = False

			lista = request.POST['lista']
			lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	 
			try:
				lista_personal.contenido.get(codigo=pelicula.codigo)
				messages.info(request,"la pelicula ya esta en esta lista")
			except:
				lista_personal.contenido.add(pelicula)
				messages.info(request,"la pelicula fue agregada con exito")

		except:
			pelicula = None		
		
		authentication = True
		context={'authentication':authentication,'user':usuario, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'listasPersonalizadas': listasPersonalizadas}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

class EliminarDeListaPersonal(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		lista = request.session['lista']
		codigo = args[0]
		lista_personal = Lista_personal.objects.get(nombre=lista, email=nombre)	
		listaEliminar = lista_personal.contenido
		pelicula = Pelicula.objects.get(codigo=codigo)
		try:
			listaEliminar.remove(pelicula) 
			messages.info(request,"Se elimino con exito")
		except:
			messages.info(request,"La pelicula ya no se encuentra")

		listas = []
		vistas = lista_personal. get_contenido()
		codigos = vistas.split(",")
		listaPersonal =[]
		for i in codigos:
			try:
				pelicula = Pelicula.objects.get(codigo=i)
				listaPersonal.append(pelicula)
			except:
				print "Hay error"

		ten = {'nombre':"Lista Personal: "+lista, 'lista':listaPersonal}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication,'user':usuario, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/listaPersonal.html',
			context,
			context_instance=RequestContext(request))
	

class Admin(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'nombre2':nombre2, 'user':user}
		return render_to_response(
			'users/admin.html',
			context,
			context_instance=RequestContext(request))

class AdminAuditor(TemplateView):
	def get(self,request,*args, **kwargs):
		form = GetRegister()
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'authentication':authentication, 'nombre':nombre,'form':form, 'user':user}
		return render_to_response(
			'users/adminAuditor.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args,**kwargs):
		form = GetRegister(request.POST)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True	
		if form.is_valid():
			cd = form.cleaned_data 
			email = cd['email']
			name = cd['nombre']
			contrasena1 = cd['contrasena1']
			contrasena2 = cd['contrasena2']			
			
			if(contrasena2 == contrasena1):
				try:
					usuario_p = Usuario.objects.get(email=email)
					message = "El correo ya se a registrado anteriormente."
					
				except:
					usuario = Usuario(
						email= email,
						nombre= name,
						contrasena= contrasena1,
						tipo = "Auditor",
						)
					
					usuario.save()
					message = "El auditor fue creado con exito. "
			else:	
				message = "Las contraseñas no coinciden."
		else:
			message = "Debe llenar todos los campos"
		
		messages.info(request,message)
		context={'authentication':authentication, 'form':form,'nombre':nombre, 'user':user}
		return render_to_response(
		'users/adminAuditor.html',
		context,
		context_instance=RequestContext(request))

class ListarCalificaciones(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		if user.tipo == "Cliente":
			usuario = nombre

		calificacion = Calificacion.objects.filter(email=usuario)

		authentication = True
		context={'authentication':authentication, 'usuario':usuario, 'calificacion':calificacion,'nombre':nombre, 'user':user}
		return render_to_response(
			'users/calificaciones.html',
			context,
			context_instance=RequestContext(request))
		
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		if user.tipo == "Cliente":
			usuario = nombre
		if user.tipo == "admin":
			usuario = request.POST['usuario']

		calificacion = Calificacion.objects.filter(email=usuario)

		authentication = True
		context={'authentication':authentication, 'usuario':usuario, 'calificacion':calificacion,'nombre':nombre, 'user':user}
		return render_to_response(
			'users/calificaciones.html',
			context,
			context_instance=RequestContext(request))

class ListasAdmin(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)

		users = Usuario.objects.filter(tipo="Cliente")
		generos = Genero.objects.all()

		authentication = True
		context={'authentication':authentication,'generos':generos, 'users':users, 'nombre':nombre, 'user':user}
		return render_to_response(
			'users/listas.html',
			context,
			context_instance=RequestContext(request))

class Recomendaciones(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		lista = generarRecomendaciones(nombre, user)
		listas = []
		authentication = True
		ten = {'nombre':"Recomendaciones: (lo mejor solo para ti)", 'lista':lista}
		listas.append(ten)

		context={'authentication':authentication, 'nombre':nombre, 'user':user, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class MasVistasUltimoMes(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		matriz = peliculasMasVistasUltimoMes()
		authentication = True
		context={'authentication':authentication, 'matriz':matriz, 'nombre':nombre, 'user':user}
		return render_to_response(
			'users/vistasUltimoMes.html',
			context,
			context_instance=RequestContext(request))

class GenerosMasVistosUltimoMes(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		matriz = generosMasVistosUltimoMes()
		authentication = True
		context={'authentication':authentication, 'matriz':matriz, 'nombre':nombre, 'user':user}
		return render_to_response(
			'users/generosVistosUltimoMes.html',
			context,
			context_instance=RequestContext(request))

class ListarVistasPorGenero(TemplateView):
	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		users = Usuario.objects.filter(tipo="Cliente")
		authentication = True
		generos = Genero.objects.all()
		if user.tipo == "admin":
			usuario = request.POST['usuario']
			url = 'users/listas.html'
			context={'authentication':authentication,'generos':generos, 'users':users, 'nombre':nombre, 'user':user}
		elif user.tipo == "Cliente":
			usuario = nombre
			url = 'users/listasCliente.html'
			listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
			context={'authentication':authentication, 'generos':generos, 'nombre':nombre, 'listasPersonalizadas':listasPersonalizadas , 'user':user}

		genero = request.POST['genero']
		usuario2 = Usuario.objects.get(email=usuario)
		vistas = usuario2.get_vistas()
		vistas2 = vistas.split(',')
		lista=[]
		for i in vistas2:
			try:
				pelicula = Pelicula.objects.get(codigo=i)
				generos = pelicula.generos.all()
				for e in generos:
					if e.nombre == genero:
						lista.append(pelicula)
			except:
				pass			
		
		cantidad = len (lista)
		
		message = "El usuario "+usuario+" ha visto "+ str(cantidad) + " peliculas del genero "+genero
		messages.info(request,message)

		
		return render_to_response(
			url,
			context,
			context_instance=RequestContext(request))

class ListarTodasLasPeliculas(TemplateView):

	def post(self,request,*args, **kwargs):		
		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)	
		peliculas = Pelicula.objects.all()	
		listas = []
		ten = {'nombre':"Todas las peliculas ", 'lista':peliculas}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication, 'user':usuario, 'nombre':nombre, 'listas':listas}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class ListarColeccion(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		listas = []
		coleccionP =[]
		coleccion = Coleccion.objects.get(email=user)
		coleccion_peliculas = coleccion.get_contenido()
		codigos = coleccion_peliculas.split(",")
		try:
			for i in codigos:
				pelicula = Pelicula.objects.get(codigo=i)
				coleccionP.append(pelicula)

		except:
				messages.info(request,"No hay peliculas en la coleccion")

		ten = {'nombre':"Su Coleccion de peliculas", 'lista':coleccionP}
		listas.append(ten)
		
		authentication = True
		context={'authentication':authentication, 'nombre':nombre, 'listas':listas, 'user':user}
		return render_to_response(
			'movies/inicio.html',
			context,
			context_instance=RequestContext(request))

class AgregarColeccion(TemplateView):
	def get(self,request,*args, **kwargs):

		nombre = request.session['emailUser']
		usuario = Usuario.objects.get(email=nombre)
		ver = True
		vista = True
		col = True
		
		pelicula = Pelicula.objects.get(codigo=args[0])

		porver = usuario.get_porver()
		tipos2 = porver.split(",")
		for i in tipos2:
			if i == pelicula.codigo:
				ver = False

		try:
			calificacion = Calificacion.objects.get(email=user,codigo=pelicula)
			cal=calificacion.valor_Calificacion + "Estrellas"
		except:
			cal="no ha sido calificado"

		vistas1 = usuario.get_vistas()
		tipos1 = vistas1.split(",")
		for i in tipos1:
			if i == pelicula.codigo:
				vista = False

		coleccion = Coleccion.objects.get(email=usuario)
		coleccion_peliculas = coleccion.get_contenido()
		codigos = coleccion_peliculas.split(",")
		for i in codigos:
			if i == pelicula.codigo:
				col = False
		if col:
			coleccion.contenido.add(pelicula)
			messages.info(request,"agregado a coleccion")
			col=False
		else:
			messages.info(request,"ya estaba en la coleccion")
				
		authentication = True
		context={'cal':cal,'col':col, 'authentication':authentication, 'nombre':nombre, 'pelicula':pelicula, 'ver':ver, 'vista':vista, 'user':usuario}
		return render_to_response(
			'movies/infoPelis.html',
			context,
			context_instance=RequestContext(request))

class Estadisticas(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		vistas = peliculasVistasEst()
		ver = peliculasPorVerEst()
		calificadas = peliculasCalificadasEst()
		colecciones = peliculasEnColecciones()
		registro = numeroRegistros()
		authentication = True
		context={'vistas':vistas,'ver':ver,'calificadas':calificadas,'colecciones':colecciones,'registro':registro ,'authentication':authentication,'nombre':nombre, 'user':user}
		return render_to_response(
			'users/estadisticas.html',
			context,
			context_instance=RequestContext(request))

class PeliculasPorCine(TemplateView):
	def get(self,request,*args, **kwargs):
		cines = Cine.objects.all()
		lista = []
		for i in cines:
			matriz = []
			cond = True
			vistas = CineVista.objects.filter(cine=i)
			for e in vistas:
				for u in matriz:
					if u[1] == e.codigo:
						u[0] = u[0] + 1
						cond = False
						break
				if cond:
					tam=len(matriz)
					matriz.append([])
					matriz[tam].append(1)
					matriz[tam].append(e.codigo)
			matriz.sort(reverse=True)
			matriz2=[]
			for z in matriz:
				if z[0] != 0:
					dic = {'cantidad':z[0], 'pelicula':z[1]}
					matriz2.append(dic)
			cine = CineClass(i.nombre, matriz2)
			lista.append(cine)
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		authentication = True
		context={'lista':lista,'authentication':authentication,'nombre':nombre, 'user':user}
		return render_to_response(
			'users/cines.html',
			context,
			context_instance=RequestContext(request))

class Editar(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		generosMasVistosUltimoMes()
		authentication = True
		context={'authentication':authentication,'nombre':nombre, 'nombre2':nombre2, 'user':user}
		return render_to_response(
			'users/editar.html',
			context,
			context_instance=RequestContext(request))

	def post(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		generosMasVistosUltimoMes()
		authentication = True
		cond = False
		name = request.POST['name']
		contrasena1 = request.POST['contrasena1']
		contrasena2 = request.POST['contrasena2']
		if name != "":
			user.nombre=name
			cond = True
		if contrasena1 != "" or contrasena2 != "":
			if contrasena1 == contrasena2:
				user.contrasena = contrasena1
				cond = True
		if cond:
			if name != "":
				request.session['nombre']=name
				nombre2 = name
			
			user.save()
			URL = 'users/cliente.html'
			messages.info(request,"Datos modificados correctamente")
		else:
			URL = 'users/editar.html'
			messages.info(request,"Los datos no fueron modificados")

		context={'authentication':authentication,'nombre':nombre, 'nombre2':nombre2, 'user':user}
		return render_to_response(
			URL,
			context,
			context_instance=RequestContext(request))

class ListasCliente(TemplateView):
	def get(self,request,*args, **kwargs):
		nombre = request.session['emailUser']
		user = Usuario.objects.get(email=nombre)
		nombre2 = request.session['nombre']
		authentication = True
		listasPersonalizadas =  Lista_personal.objects.filter(email=nombre)
		generos = Genero.objects.all()
		context={'authentication':authentication, 'generos':generos, 'nombre':nombre, 'nombre2':nombre2, 'listasPersonalizadas':listasPersonalizadas , 'user':user}
		return render_to_response(
			'users/listasCliente.html',
			context,
			context_instance=RequestContext(request))