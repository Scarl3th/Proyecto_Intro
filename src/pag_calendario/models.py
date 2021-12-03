from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Modelo para crear eventos
class eventos(models.Model):
    nombre = models.CharField(max_length=120)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null = True,)
    prioridad = models.IntegerField(default = 1, validators=[MaxValueValidator(10, message="Debe ingresar una prioridad dentro del rango (1-10)"), MinValueValidator(1, message="Debe ingresar una prioridad dentro del rango (1-10)")])
    ramo = models.CharField(max_length=120)

#Modelo para eliminar eventos
class eliminar(models.Model):
    event_id = models.IntegerField()