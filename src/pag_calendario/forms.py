from django import forms
from django.db.models import query
from .models import eventos, eliminar
from randp.models import Ramos_y_preferencias

class formularioEventos(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Nombre de la evaluacion..." }))
    fecha  = forms.DateField(widget=forms.DateInput(attrs={"placeholder" : "aaaa-mm-dd" }))
    descripcion  = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Ingrese una descripcion de su evaluacion", "rows": 15, "cols": 50}))
    prioridad = forms.IntegerField(widget = forms.TextInput(attrs = {"placeholder" : "Prioridad de la evaluacion 1-10", "size": 30 }))
    
    ramo = forms.ChoiceField(choices = [("luego será reescrito", "asi que no importa")])

    class Meta:
        model = eventos
        fields = ['nombre', 'fecha', 'descripcion', 'prioridad', 'ramo']

    #Sirve para poner self.request
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(formularioEventos, self).__init__(*args, **kwargs)

        #Sobrescribimos ramo
        opciones = []
        for ramo in Ramos_y_preferencias.objects.filter(usuario = self.user):
            opciones.append((ramo.nombre, ramo.nombre))

        self.fields['ramo'].choices = opciones
        self.fields['descripcion'].label = "aa"

    
    def clean_prioridad(self, *args, **kwargs):
        numero = self.cleaned_data.get('prioridad')
        if numero > 10 or numero < 1:
            raise forms.ValidationError("Debe ingresar una prioridad dentro del rango (1-10)")
        else:
            return numero

    def clean_ramo(self, *args, **kwargs):
        
        lista_objetos = Ramos_y_preferencias.objects.filter(usuario = self.user)
        lista_ramos = []
        for objeto in lista_objetos:
            lista_ramos.append(objeto.nombre)

        ramo_evento = self.cleaned_data.get("ramo")
        print("nombre del ramo", ramo_evento)
        if ramo_evento in lista_ramos:
            return ramo_evento
        else:
            raise forms.ValidationError("No está registrado ese ramo")


class eliminarEvento(forms.Form):
    opciones = []
    for evento in eventos.objects.all():
        opciones.append((evento.nombre, evento.nombre))
    
    event_id = forms.ChoiceField(choices = opciones)
    class Meta:
        model = eliminar
        fields = ['event_id']

    #Sirve para poder poner self.request
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(eliminarEvento, self).__init__(*args, **kwargs)

        opciones = []
        for evento in eventos.objects.filter(usuario = self.request.user):
            opciones.append((evento.nombre, evento.nombre))

        #Overwrite el field event id para poder poner self.request.user:
        self.fields['event_id'].choices = opciones
        self.fields['event_id'].label = "Elimine una evaluacion:"
        

    def clean_event_id(self, *args, **kwargs):
        nombre = self.cleaned_data.get("event_id")
    
        if nombre in eventos.objects.filter(usuario = self.request.user).values_list('nombre', flat=True):
            return nombre
        else:
         
            raise forms.ValidationError("No existe un evento con ese id")

