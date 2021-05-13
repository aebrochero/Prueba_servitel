from Main_Check.models import Receta
from rest_framework import serializers

class RecetaSerializer(serializers.HyperlinkedModelSerializer):
    
     class Meta:
         model=Receta
         fields=['id','nombre','ingredientes','autor','rating','valor','origen','calorias','fecha_publicacion']
