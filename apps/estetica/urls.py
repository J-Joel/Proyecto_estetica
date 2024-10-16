from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio, name="inicio"), # Funciones
    path("", views.Inicio.as_view(), name="inicio"), # Clases
    path("contacto/", views.Contacto.as_view(), name="contacto"), # Clases
]
