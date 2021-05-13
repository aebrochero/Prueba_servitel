from Main_Check.models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta: #porque nombre meta: Clase propia en framework.
         model=Cliente
         fields=['nombre_cliente','apellido_cliente','direccion','telefono','correo_cliente','contraseña_cliente','fecha_creacion_cliente','foto']