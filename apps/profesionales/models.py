from django.db import models
from ..usuarios.models import Telefono

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=50, blank=True)
    apellido = models.CharField('Apellido', max_length=50, blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField('Email', max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
