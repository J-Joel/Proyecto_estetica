from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio, name="inicio"), # Funciones
    path("", views.Inicio.as_view(), name="inicio"), # Clases
    path("contacto/", views.Contacto.as_view(), name="contacto"), # Clases
    path("galeria/", views.Galeria.as_view(), name="galeria"),
    path("profesionales/", views.Profesionales.as_view(), name="profesionales"),
    path("preguntas/", views.PreguntasFrecuentes.as_view(), name="preguntas"),
    path("ayuda/", views.ayuda.as_view(), name="ayuda"),
]
