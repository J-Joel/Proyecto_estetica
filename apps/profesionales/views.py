from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Profesionales(TemplateView):
    template_name = 'inicio/profesionales.html'