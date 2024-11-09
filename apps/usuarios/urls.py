from django.urls import path
from . import views

urlpatterns = [
    path("", views.Perfil.as_view(), name="perfil"),
    path("login/", views.Login.as_view(), name="login"),
]