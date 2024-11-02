from django.shortcuts import render # Funciones
from django.views.generic import TemplateView, ListView # Clases

# Create your views here.

#def inicio(request): # Funciones
#    return render(request,'inicio/index.html')
class Inicio(TemplateView): # Clases
    template_name = 'inicio/index.html'
    
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