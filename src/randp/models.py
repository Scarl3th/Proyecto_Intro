from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Ramos_y_preferencias(models.Model):

	ROJO = '#b52218'
	AZUL = '#2735f2'
	VERDE = '#1c731e'
	AMARILLO = '#1c731e'
	MORADO = '#8237ad'
	ROSA = '#ed55c0'
	ANARANJADO = '#ed7700'
	TURQUESA = '#2f8a73'  
	
	eleccion_colores = [
    (ROJO,'Rojo'),
    (AZUL,'Azul'),
    (VERDE,'Verde'),
    (AMARILLO,'Amarillo'),
    (MORADO,'Morado'),
    (ROSA,'Rosa'),
    (ANARANJADO,'Anaranjado'),
    (TURQUESA,'Turquesa')
    ]

	nombre = models.CharField(max_length = 40)

	prioridad = models.IntegerField(validators = [	MaxValueValidator(limit_value=10, message='Ingrese una prioridad válida'), 
        											MinValueValidator(limit_value=1, message='Ingrese una prioridad válida')]
    )
	color = models.CharField(
		max_length = 15,
		choices = eleccion_colores,
		default = ROJO 	
	)

	usuario = models.ForeignKey( User, on_delete=models.CASCADE)

class Eliminar_ramo(models.Model):
	ramo_id = models.IntegerField()


