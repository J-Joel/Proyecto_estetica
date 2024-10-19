from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class CatalogoServicios(TemplateView): # Clases
    template_name = 'servicio/catalogoservicios.html'