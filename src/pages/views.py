from django.shortcuts import render
from django.http import HttpResponse

from randp.models import Ramos_y_preferencias
from pag_calendario.models import eventos
import datetime

def dias_restantes(fecha_evaluacion):
	separado = fecha_evaluacion.split("/")
	hoy = datetime.date.today()
	dias_evaluacion = datetime.date(int(separado[2]), int(separado[1]), int(separado[0]))
    
	dias = dias_evaluacion - hoy
	return dias.days

#Create your views here.
def home_view(request,*args, **kwargs):
	n_dia = datetime.date.today().weekday()
	all_eventos = eventos.objects.filter( usuario = request.user)
	all_ramos = Ramos_y_preferencias.objects.filter( usuario = request.user)

	dic_ramos = {}
	dic_prioridades = {}

	#Crear diccionario de ramos(vacío) y prioridades 
	for ramo in all_ramos:
		dic_ramos[ramo.nombre] = {}
		dic_prioridades[ramo.nombre] = int(ramo.prioridad)

	#Rellenar diccionario ramos con los eventos
	for evento in all_eventos:
		fecha_evento = evento.fecha.strftime("%d/%m/%Y")
		dic_ramos[evento.ramo][evento.nombre] = [fecha_evento, evento.prioridad]

	#Lista de listas que representa los dias de la semana
	#En la "sub-lista" deben ir los eventos
	organizacion = [[],[],[],[],[],[],[]]

	for ramo in dic_ramos:
		for evaluacion in dic_ramos[ramo]:
			dias = dias_restantes(dic_ramos[ramo][evaluacion][0])

			#Cuántos dias antes de la evaluacion va a aparecer en la organización
			prioridad_total = dic_ramos[ramo][evaluacion][1] * dic_prioridades[ramo]
			dias_aviso = round(prioridad_total*0.2 +0,8)

			#Condicional para ver si se debe mostrar la evaluacion
			if (dias-7 <= dias_aviso):

				#el avance es cuanto se le suma a n_dia, para que sea el index de organizacion
				avance = dias - dias_aviso

				#Los siguientes condicionales aseguran que no existan errores
				if avance < 0:
					avance = 0
				dia_calendario = avance + n_dia
				if dia_calendario > 6:
					dia_calendario = dia_calendario%7

				print(dia_calendario)

				#Se añade la evaluacion al dia de la semana correspondiente
				organizacion[int(dia_calendario)].append(evaluacion)

	return render(request,"home.html", {"lista_dias" : organizacion})

def inicio_view(request,*args, **kwargs):
	return render(request,"iniciar_sesion.html", {})

def cuenta_view(request,*args, **kwargs):
	return render(request, 'cuenta.html', {})

def calendar_view(*args, **kwargs):
	return HttpResponse('<h1>Calendario</h1>')

def config_view(request,*args, **kwargs):
	return render(request,"config.html", {})

def perfil_view(request, *args, **kwargs):
	return render(request,'perfil.html', {})

def ramos_view(request, *args, **kwargs):
	return render(request,'ramos.html', {})
