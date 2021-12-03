from django.shortcuts import render
from django.http import HttpResponse
#from randp.models import Ramos_y_preferencias

# Create your views here.
def home_view(request,*args, **kwargs):
	#obj = Ramos_y_preferencias.objects.get(id=2)
	#context = {'object':obj}
	return render(request,"home.html", {})

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
