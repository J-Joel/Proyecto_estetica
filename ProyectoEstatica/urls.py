
# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar desde django.urls
from .settings.local import STATIC_URL,STATIC_ROOT # Cargo una variable?
from django.conf.urls.static import static # Cargo una clase?
from path import urlsglobal

# Revisen la carpeta path, ahi se importan cada archivo url de las apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlsglobal.estetica), name='inicio'),  # Define la vista para la página de inicio
    path('usuarios/', include(urlsglobal.usuarios), name='usuarios'),
    path('profesionales/', include(urlsglobal.profesionales), name='profesionales'),
    path('servicios/', include(urlsglobal.servicios), name='servicios'),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)