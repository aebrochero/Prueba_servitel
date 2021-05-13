# Register your models here.

from django.contrib import admin
from Main_Check.models import Receta
from Main_Check.models import Cliente

# admin.site.register(Receta)
@admin.register(Receta) #@ es un decorador SOLO PARA LA CLASE, clase abajo de decorador
class RecetaAdmin(admin.ModelAdmin):
    fields=('nombre','ingredientes','autor','rating','valor','origen','calorias','fecha_publicacion') #nombramos los campos necesarios para Receta (podemos usar o no todos los campos)
    list_display=('id','nombre','ingredientes','autor','rating','valor','origen','calorias','fecha_creacion','fecha_modificacion','fecha_publicacion') #colocar los campos necesarios a mostrar

@admin.register(Cliente) #@ es un decorador SOLO PARA LA CLASE, clase abajo de decorador
class ClienteAdmin(admin.ModelAdmin):
    fields=('nombre_cliente','apellido_cliente','direccion','telefono','correo_cliente','contraseña_cliente','foto')
    list_display=('id','nombre_cliente','apellido_cliente','telefono','correo_cliente','fecha_creacion_cliente','foto')


