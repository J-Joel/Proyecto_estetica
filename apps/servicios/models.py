from django.db import models

# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50, blank = True)
    descripcion = models.TextField('Descripción',max_length=100)
    duracion = models.IntegerField() # Duración en minutos o Horas
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
