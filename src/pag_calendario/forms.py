from django import forms
from .models import eventos, eliminar

class formularioEventos(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Nombre de la evaluacion..." }))
    fecha  = forms.DateField(widget=forms.DateInput(attrs={"placeholder" : "aaaa-mm-dd" }))
    descripcion  = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Ingrese una descripcion de su evaluacion", "rows": 15, "cols": 50}))
    prioridad = forms.IntegerField(widget = forms.TextInput(attrs = {"placeholder" : "Prioridad de la evaluacion 1-10", "size": 30 }))

    class Meta:
        model = eventos
        fields = ['nombre', 'fecha', 'descripcion', 'prioridad']

        def clean_prioridad(self, *args, **kwargs):
            numero = self.cleaned_data.get('prioridad')
            if numero > 10 or numero < 1:
                raise forms.ValidationError("Debe ingresar una prioridad dentro del rango (1-10)")
            else:
                return numero

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