from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

#Modelo para crear eventos
class eventos(models.Model):
    nombre = models.CharField(max_length=120)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null = True,)
    prioridad = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

#Modelo para eliminar eventos
class eliminar(models.Model):
    event_id = models.IntegerField()