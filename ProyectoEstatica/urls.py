
# ProyectoEstatica/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar desde django.urls
from .settings.local import STATIC_URL,STATIC_ROOT # Cargo una variable?
from django.conf.urls.static import static # Cargo una clase?
from path import urlsglobal
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

# Revisen la carpeta path, ahi se importan cada archivo url de las apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlsglobal.estetica), name='inicio'),  # Define la vista para la página de inicio
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),  # Vista de login
    path('profesionales/', include(urlsglobal.profesionales), name='profesionales'),
    path('servicios/', include(urlsglobal.servicios), name='servicios'),  # Vista de login
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)