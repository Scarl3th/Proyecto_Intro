from django.shortcuts import render
from django.http import HttpResponse
from .models import eventos
from .forms import formularioEventos, eliminarEvento
from randp.models import Ramos_y_preferencias

# Create your views here.
def calendario_view(request):
    objetos = eventos.objects.all()
    contexto = []

    for objeto in objetos:
        dic = {}
        dic["id"] = str(objeto.nombre)
        dic["date"] = str(objeto.fecha.strftime("%m/%d/%Y"))
        dic["name"] = str(objeto.nombre)
        dic["description"] = str(objeto.descripcion) 
        dic["type"] = "event"
        contexto.append(dic)

    return render(request, "calendario_view.html", {"eventos":contexto})
    #No se cm chucha sabe donde buscar el template
    #Si sale error en settings añadir la carpeta templates
    #de la app

#view que renderiza los formularios:
def formularioEventos_view(request):
    #Formulario para ingresar eventos
    form = formularioEventos(request.POST or None, user = request.user)

    if form.is_valid():
        #Cuatro lineas siguientes permiten que sea para el usuario
        evnt = form.save(commit=False)
        evnt.usuario = request.user  
        evnt.save()
        form = formularioEventos(user = request.user) #Añadir esto de user = request.user pk normalmente se elimina
    

    #Formulario para eliminar eventos

    form1 = eliminarEvento(request.POST or None, request = request)
    if form1.is_valid():
    
        evento = eventos.objects.filter(usuario = request.user).filter(nombre =  form1['event_id'].value())
        evento = evento[0]
        evento.delete()

        form1 = eliminarEvento(request = request)

    context = {
        'form' : form,
        'form1' : form1,
    }

    return render(request, "formularioEventos.html", context)