from django.shortcuts import render # Funciones
from django.views.generic import TemplateView, ListView # Clases

# Create your views here.
#def login(request):
#    return render(request,'usuarios/login.html')
class Login(TemplateView):
    template_name = 'usuarios/login.html'