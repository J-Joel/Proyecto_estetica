
# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar desde django.urls
from django.conf import settings # Cargo una variable?
from django.conf.urls.static import static # Cargo una clase?
from path import urlsglobal

# Revisen la carpeta path, ahi se importan cada archivo url de las apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlsglobal.estetica), name='inicio'),  # Define la vista para la página de inicio
    path('login/', include(urlsglobal.usuarios), name='login'),  # Vista de login
    path('profesionales/', include(urlsglobal.profesionales), name='profesionales'),
    path('servicios/', include(urlsglobal.servicios), name='servicios'),  # Vista de login
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)