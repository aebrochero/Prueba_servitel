from Main_Check.models import Receta
from Main_Check.serializers.recetaSerializer import RecetaSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class RecetaViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = Receta.objects.all() #consulta db
    # serializer_class = RecetaSerializer

    def list(self, request):
        queryset = self.queryset
        print("queryset---> ", queryset) 
        serializer = RecetaSerializer(queryset, many=True)
        print("serializer --> ",serializer.data)
        return Response(serializer.data)


    def create(self, request):
        #tarea realizar POST o create
        
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass