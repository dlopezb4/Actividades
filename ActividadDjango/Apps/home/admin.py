from django.contrib import admin
from .models import Administradores, Cliente, Estudiante,TipoCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Estudiante)
admin.site.register(Administradores)
