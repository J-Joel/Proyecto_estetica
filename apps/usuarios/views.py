from django.shortcuts import render # Funciones
from django.views.generic import TemplateView, ListView # Clases
from django.shortcuts import render, redirect
from .models import Cliente
from ..servicios.models import Servicio

# Create your views here.
#def login(request):
#    return render(request,'usuarios/login.html')
class Login(TemplateView):
    template_name = 'usuario/login.html'

def Conectado(request):
    usuario = request.POST['txtuserlog'] # Los datos enviados por un formulario usando el metodo POST, se reciben a traves del request, el formulario almacena los datos de cada elemento, por su nombre
    contraseña = request.POST['txtpasslog']

    usuario = Cliente.objects.filter(usuario=usuario, contraseña=contraseña)
    servicios = Servicio.objects.all()
    return render(request, 'inicio/index.html', {"usuario": usuario,"servicios":servicios,})

def RegistrarUsuario(request):
    usuario = request.POST['txtuserreg'] # Los datos enviados por un formulario usando el metodo POST, se reciben a traves del request, el formulario almacena los datos de cada elemento, por su nombre
    contraseña = request.POST['txtpassreg']
    email = request.POST['txtemailreg']

    Cliente.objects.create(usuario = usuario, contraseña = contraseña, email = email) # El metodo create, se encarga directamente de eso, ademas de guardarlo en la base de datos
    return redirect('login')

class Perfil(TemplateView):
    pass
