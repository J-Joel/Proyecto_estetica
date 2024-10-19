from django.urls import path
from . import views


urlpatterns = [
    path("profesionales/", views.Profesionales.as_view(), name="profesionales"),
]
