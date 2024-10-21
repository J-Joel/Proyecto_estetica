from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfesionalesView.as_view(), name='profesionales'),       
]
