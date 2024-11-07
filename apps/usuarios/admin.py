from django.contrib import admin
from .models import Telefono, Cliente 
# Register your models here.
class   telefonoAdmin (admin.ModelAdmin):
    list_display= ('numero','tipo')
    list_filter = ['tipo']
    
admin.site.register(Telefono,telefonoAdmin)

# Register your models here.
class clienteAdmin (admin.ModelAdmin):
    list_display= ('dni','nombre','apellido','email')
    search_fields = ['dni','nombre', 'apellido']
    
admin.site.register(Cliente,clienteAdmin)
