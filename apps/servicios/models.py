from django.db import models
from django.shortcuts import render

# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=100, blank = True)
    descripcion = models.TextField('Descripción',max_length=5000)
    duracion = models.IntegerField('Duración (en horas)') # Duración en minutos o Horas
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    def listar_servicios(request):
        # Obtiene todos los servicios de la base de datos
        servicios = Servicio.objects.all()
        return render(request, 'listar_servicios.html', {'servicios': servicios})