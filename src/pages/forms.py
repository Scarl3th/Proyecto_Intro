from django import forms
from randp.models import Ramos_y_preferencias, Eliminar_ramo

class Randp_form(forms.ModelForm):
    class Meta:
        model = Ramos_y_preferencias
        fields = ['nombre', 'prioridad', 'color'] 

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Randp_form, self).__init__(*args, **kwargs)

    #Evitaremos que se puedan ingresar dos ramos con el mismo nombre
    def clean_nombre(self, *args, **kwargs):
        #nombre del ramo
        a = self.cleaned_data.get("nombre")
        lista = [] #Lista de los ramos de la base de datos
        for b in Ramos_y_preferencias.objects.filter(usuario = self.user).values_list('nombre', flat = True):
            lista.append(b)

        if a in lista:
            raise forms.ValidationError("Ya existe un ramo con ese nombre")
        else:
            return a


class Eliminar_ramo_form(forms.Form):
    #Creo que esto se sobreescribe en __int__
    opciones = []
    for ramo in Ramos_y_preferencias.objects.all():
        opciones.append((ramo.nombre, ramo.nombre))

    ramo_id = forms.ChoiceField(choices=opciones)

    class Meta:
        model = Eliminar_ramo
        fields = ['ramo_id']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Eliminar_ramo_form, self).__init__(*args, **kwargs)

        opciones = []
        for ramo in  Ramos_y_preferencias.objects.filter(usuario = self.user):
            opciones.append((ramo.nombre, ramo.nombre))

        #Sobreescribimos:
        self.fields['ramo_id'].choices = opciones
        self.fields['ramo_id'].label = "Elimine un ramo:"

    #No es necesario, antes se ingresaba de manera manual, ahora es con una lista de seleccion
    def clean_ramo_id(self, *args, **kwargs):
        nombre = self.cleaned_data.get("ramo_id")
        if nombre in Ramos_y_preferencias.objects.filter(usuario = self.user).values_list('nombre', flat=True):
            return nombre
        else:
            raise forms.ValidationError("No existe ese ramo")


        
    

    
