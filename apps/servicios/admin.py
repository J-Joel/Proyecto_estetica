from django.contrib import admin
from.models import Servicio

# Register your models here.
class serviAdmin (admin.ModelAdmin):
    list_display= (
        'nombre',
        'descripcion',
        'duracion',
        'precio',
    )
    
    search_fields = ['nombre', 'apellido']
admin.site.register(Servicio, serviAdmin)
    