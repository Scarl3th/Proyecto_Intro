from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"home.html", {})

def inicio_view(*args, **kwargs):
	return HttpResponse('<h1>Iniciar Sesión</h1>')

def cuenta_view(*args, **kwargs):
	return HttpResponse('<h1>Crear Cuenta</h1>')

def calendar_view(*args, **kwargs):
	return HttpResponse('<h1>Calendario</h1>')

def config_view(*args, **kwargs):
	return HttpResponse('<h1>Configuración</h1>')

def perfil_view(*args, **kwargs):
	return HttpResponse('<h1>Perfil</h1>')

def ramos_view(*args, **kwargs):
	return HttpResponse('<h1>Ramos</h1>')
