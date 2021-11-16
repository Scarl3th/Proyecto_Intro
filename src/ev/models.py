from django.db import models

# Create your models here.
class Ramos(models.Model):
	ROJO = '#b52218'
	AZUL = '#2735f2'
	VERDE = '#1c731e'
	AMARILLO = '#1c731e'
	MORADO = '#8237ad'
	ROSA = '#ed55c0'
	ANARANJADO = '#ed7700'
	TURQUESA = '#2f8a73'  
	eleccion_colores = [
    (ROJO,'Rojo')
    (AZUL,'Azul')
    (VERDE,'Verde')
    (AMARILLO,'Amarillo')
    (MORADO,'Morado')
    (ROSA,'Rosa')
    (ANARANJADO,'Anaranjado')
    (TURQUESA,'Turquesa')
    ]

	nombre = models.CharField(max_length = 40)

	prioridad = models.IntegerField(validation = [	MaxValueValidator(limit_value=10, message='Ingrese una prioridad válida'), 
        											MinValueValidator(limit_value=1, message='Ingrese una prioridad válida')]
    )
	color = models.CharField(
		max_length = 15,
		choices = eleccion_colores,
		default = ROJO 	
	)
