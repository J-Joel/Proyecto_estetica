
# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar desde django.urls
from path import urlsglobal

# Revisen la carpeta path, ahi se importan cada archivo url de las apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlsglobal.estetica), name='inicio'),  # Define la vista para la página de inicio
    path('login/', include(urlsglobal.usuarios), name='login'),  # Vista de login
    path('servicios/', include(urlsglobal.servicios), name='servicios'),  # Vista de login
]
