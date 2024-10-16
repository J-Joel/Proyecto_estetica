
# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path  # Asegúrate de importar desde django.urls
from . import views  # Importa tus vistas
from ProyectoEstatica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.InicioView.as_view(), name='inicio'),  # Define la vista para la página de inicio
    path('login/', views.LoginView.as_view(), name='login'),  # Vista de login
    #path('contacto/', views.contactoView.as_view(), name='contacto'),  # Vista para contacto  

]
