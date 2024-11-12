from django.shortcuts import render # Funciones
from django.views.generic import TemplateView, ListView # Clases
from ..servicios.models import Servicio

# Create your views here.

#def inicio(request): # Funciones
#    return render(request,'inicio/index.html')
class Inicio(TemplateView): # Clases
    template_name = 'inicio/index.html'

    def get_context_data(self): 
        servicios = Servicio.objects.all() # Recibe todo los registros del modelo
        return {"servicios":servicios,} # Envia un listado como diccionario
    
class Contacto(TemplateView):
    template_name = 'inicio/contacto.html'
    
class Galeria(TemplateView):
    template_name = 'inicio/galeria.html'
    
class Profesionales(TemplateView):
    template_name = 'inicio/profesionales.html'

class PreguntasFrecuentes(TemplateView):
    template_name = "inicio/preguntas_frecuentes.html"
    
class Ayuda(TemplateView):
    template_name = "inicio/ayuda.html"