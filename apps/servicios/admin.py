from django.contrib import admin
from.models import Servicio

# Register your models here.
class servAdmin (admin.ModelAdmin):
    list_display= ()
admin.site.register(Servicio)
