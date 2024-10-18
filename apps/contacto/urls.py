# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path  # Asegúrate de importar desde django.urls
from . import views  # Importa tus vistas
from contacto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto.as_view(), name='contacto'),  # Vista para contacto  
]