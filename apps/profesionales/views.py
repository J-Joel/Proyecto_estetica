from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProfesionalesView(TemplateView):
    template_name = 'inicio/profesionales.html'