from django.urls import path
from . import views

urlpatterns = [
    path("", views.CatalogoServicios.as_view(), name="servicios"), # Clases

]
