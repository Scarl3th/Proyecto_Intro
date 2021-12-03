from django import forms
from .models import eventos, eliminar
from randp.models import Ramos_y_preferencias

class formularioEventos(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Nombre de la evaluacion..." }))
    fecha  = forms.DateField(widget=forms.DateInput(attrs={"placeholder" : "aaaa-mm-dd" }))
    descripcion  = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Ingrese una descripcion de su evaluacion", "rows": 15, "cols": 50}))
    prioridad = forms.IntegerField(widget = forms.TextInput(attrs = {"placeholder" : "Prioridad de la evaluacion 1-10", "size": 30 }))
    ramo = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Ramo al que pertenece el evento", 'size': 50 }))

    class Meta:
        model = eventos
        fields = ['nombre', 'fecha', 'descripcion', 'prioridad', 'ramo']

    def clean_prioridad(self, *args, **kwargs):
        numero = self.cleaned_data.get('prioridad')
        if numero > 10 or numero < 1:
            raise forms.ValidationError("Debe ingresar una prioridad dentro del rango (1-10)")
        else:
            return numero
  
    def clean_ramo(self, *args, **kwargs):
        lista_objetos = Ramos_y_preferencias.objects.all()
        lista_ramos = []
        for objeto in lista_objetos:
            lista_ramos.append(objeto.nombre)

        ramo_evento = self.cleaned_data.get('ramo')    
        if ramo_evento in lista_ramos:
            return self.cleaned_data.get('ramo')
        else:
            raise forms.ValidationError("No existe ese ramo")

    

class eliminarEvento(forms.ModelForm):
    class Meta:
        model = eliminar
        fields = ['event_id']

    def clean_event_id(self, *args, **kwargs):
        idevent = self.cleaned_data.get("event_id")
        if idevent in eventos.objects.values_list('id', flat=True):
            return idevent
        else:
            raise forms.ValidationError("No existe un evento con ese id")