import re
from django.db import models
from django.core.exceptions import ValidationError 
 
# Modelo Telefono 
class Telefono(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=15)
    tipo = models.CharField(
        max_length=10,
        choices=[('movil', 'Móvil'), ('fijo', 'Fijo')],
        default='movil'
    )

    def clean(self):
        # Validación simple para el formato del número de teléfono
        if not re.match(r'^\+?[\d\s()-]{7,15}$', self.numero):
            raise ValidationError("El número de teléfono no tiene un formato válido.")

    def __str__(self):
        return f'{self.tipo.capitalize()} - {self.numero}'

#Modelo Cliente
class Cliente(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni= models.CharField('DNI', max_length=50)
    nombre= models.CharField('Nombre', max_length=50)
    apellido= models.CharField('Apellido', max_length=50)
    telefono= models.ForeignKey(Telefono, on_delete=models.SET_NULL, null=True, blank=True)
    email= models.CharField(max_length=100, unique=True)
    
    def __str__(self):
     return f"{self.nombre} {self.apellido}" 
 


