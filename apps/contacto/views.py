from django.shortcuts import render
from django.views.generic import TemplateView, ListView # Clases

class contacto(TemplateView): # Clases
    template_name = 'contacto/contacto.html'
    