from django.urls import path
from . import views

urlpatterns = [
    #path("", views.inicio, name="inicio"), # Funciones
    path("", views.Inicio.as_view(), name="inicio"), # Clases

]
