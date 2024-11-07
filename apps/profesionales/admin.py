from django.contrib import admin
from .models import Empleado

# Register your models here.
class servAdmin (admin.ModelAdmin):
    list_display= ()
admin.site.register(Empleado)
    
    