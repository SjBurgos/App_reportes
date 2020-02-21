from django.db import models

# Create your models here.
class Persona(models.Model):
    apellido = models.CharField(
        max_length=50
    )
    nombre = models.CharField(
        max_length=50
    )
    dni = models.PositiveIntegerField()
    telefono = models.CharField(
        max_length=25
    )
    email = models.EmailField(
        max_length=75
    )