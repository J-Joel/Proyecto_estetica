# ProyectoEstatica/views.py
from django.shortcuts import render
from django.views.generic import TemplateView, ListView # Clases

class InicioView(TemplateView):
    def get(self, request):
        # Lógica para la vista de inicio
        return render(request, 'inicio/index.html')

class LoginView(TemplateView):
    def get(self, request):
        # Lógica para la vista de login
        return render(request, 'usuarios/login.html')

class GaleriaView(TemplateView):
    def get(self, request):
        # Lógica para la vista de inicio
        return render(request, 'inicio/galeria.html')
