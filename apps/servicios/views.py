from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Servicio

# Create your views here.
class CatalogoServicios(TemplateView): # Clases
    template_name = 'servicio/catalogoservicios.html'

    def get_context_data(self): 
        servicios = Servicio.objects.all() # Recibe todo los registros del modelo
        return {"servicios":servicios,} # Envia un listado como diccionario