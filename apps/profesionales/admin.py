from django.contrib import admin
from .models import Empleado

# Register your models here.
class servAdmin (admin.ModelAdmin):
    list_display= (
        'nombre',
        'apellido',
        'email',
    )
    
    search_fields = ['nombre', 'apellido']
admin.site.register(Empleado, servAdmin)
    
    