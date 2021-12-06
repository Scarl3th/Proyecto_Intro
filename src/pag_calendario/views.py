from django.shortcuts import render
from django.http import HttpResponse
from .models import eventos
from .forms import formularioEventos, eliminarEvento

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
    form = formularioEventos(request.POST or None, request = request)
    if form.is_valid():
        #Cuatro lineas siguientes permiten que sea para el usuario
        evnt = form.save(commit=False)
        evnt.usuario = request.user  
        evnt.save()
        form = formularioEventos()

    #Formulario para eliminar eventos
    form1 = eliminarEvento(request.POST or None, request = request)
    if form1.is_valid():
        evento = eventos.objects.filter(usuario = request.user).get(pk = int(form1['event_id'].value()))
        evento.delete()
        form1 = eliminarEvento()

    context = {
        'form' : form,
        'form1' : form1,
        'lista' : eventos.objects.filter(usuario = request.user).all()
    }
    return render(request, "formularioEventos.html", context)