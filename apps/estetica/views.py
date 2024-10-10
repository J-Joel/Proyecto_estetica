from django.shortcuts import render # Funciones

from django.views.generic import TemplateView, ListView # Clases

# Create your views here.

#def inicio(request): # Funciones
#    return render(request,'inicio/index.html')
class Inicio(TemplateView): # Clases
    template_name = 'inicio/index.html'