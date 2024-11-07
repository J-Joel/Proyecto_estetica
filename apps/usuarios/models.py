from django.db import models

# Create your models here.
#Modelo Cliente
class Cliente(models.Models):
    id_usuario = models.AutoField(primary_key=True)
    dni= models.CharField('DNI', max_length=50)
    nombre= models.CharField('Nombre', max_length=50)
    apellido= models.CharField('Apellido', max_length=50)
    telefono= models.ForeignKey('Telefono', on_delete=models.SET_NULL, null=True, blank=True)
    email= models.CharField(max_length=100, unique=True)
    
    def __str__(self):
     return f"{self.nombre} {self.apellido}" 