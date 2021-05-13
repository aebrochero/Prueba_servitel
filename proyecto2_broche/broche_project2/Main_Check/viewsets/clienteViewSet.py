from Main_Check.models import Cliente
from Main_Check.serializers.clienteSerializer import ClienteSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response


class ClienteViewSet(viewsets.ViewSet):

    queryset = Cliente.objects.all() #consulta a la database de cliente


    def list(self, request):    #READ
        queryset = self.queryset
        print("queryset---> ", queryset) 
        serializer = ClienteSerializer(queryset, many=True)  #many=True serializar sobre VARIOS modelos (lista)
        print("serializer --> ",serializer.data)
        return Response(serializer.data)


    def create(self, request):  #POST

        datos=request.POST
        nombre_cliente=datos.get('nombre_cliente')
        apellido_cliente=datos.get('apellido_cliente')

        print("Nombre--->", nombre_cliente) 
        print("Apellido--->", apellido_cliente) 
        nuevo_cliente=Cliente.objects.create()
        nuevo_cliente.nombre_cliente=nombre_cliente
        nuevo_cliente.apellido_cliente=apellido_cliente
        nuevo_cliente.save()    #Guardar la informacion colocada anteriormente IMPORTANTE
        return Response('cualquier cosa', status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None): #PARTE DE READ, DETALLAR UNO http://localhost:8000/prueba-url/api-clientes/cliente/1/ --> primary key valor de id para encontrar algun recurso, si no esta el recurso, una respuesta
        content = {'Mensaje': 'NO HA FUNCIONADO'}
        queryset = self.queryset.get(id=pk)
        serializer = ClienteSerializer(queryset)   
        
        if not queryset:
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        content = {
            'Mensaje': 'SI FUNCIONO',
            'Data': serializer.data,        
        }
        return Response(content, status=status.HTTP_200_OK)

        # return Response (serializer.data)

    def update(self, request, pk=None):     #PUT
        datos=request.data      #Estos son los datos que se envian desde PostMan
        clientes = self.queryset.filter(id=pk)
        nombre_cliente =datos.get('nombre_cliente')
        apellido_cliente =datos.get('apellido_cliente')
        segundo_apellido_cliente =datos.get('segundo_apellido_cliente')
        direccion =datos.get('direccion')
        telefono =datos.get('telefono')
        correo_cliente =datos.get('correo_cliente')
        contraseña_cliente =datos.get('contraseña_cliente')

        if not clientes:
            return Response('NO ESTA EL CLIENTE', status=status.HTTP_404_NOT_FOUND)

        # cliente existe y sera actualizado

        cliente= clientes.first()                   # Obtenemos el primer modelo en la lista de n-Modelos
        cliente.nombre_cliente = nombre_cliente     # Acceder al atributo (en este caso el nombre) de ese modelo, y mi modelo es el cliente
                                                    # despues del = estamos actualizando el valor con los datos enviados desde postMan
        
        cliente.apellido_cliente = apellido_cliente
        cliente.segundo_apellido_cliente = segundo_apellido_cliente
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.correo_cliente = correo_cliente
        cliente.contraseña_cliente = contraseña_cliente

        cliente.save()                              # Guardar la informacion

        serializer = ClienteSerializer(cliente)
        content ={ 
            'Mensaje':'Encontro Cliente',
            'Datos' : serializer.data,
        }
        return Response(content, status=status.HTTP_200_OK)


    def partial_update(self, request, pk=None):     #PATCH
        pass

    def destroy(self, request, pk=None):    #DELETE
        clientes = self.queryset.filter(id=pk)

        if not clientes:
            return Response('NO ESTA EL CLIENTE', status=status.HTTP_404_NOT_FOUND)

        # cliente existe y sera actualizado

        cliente= clientes.first()           # Obtenemos el primer modelo en la lista de n-Modelos
        cliente.delete()                    # funcion delete para borrar el modelo que se obtuvo desde la variable cliente


        content ={ 
            'Mensaje':'Cliente Eliminado',
        }
        return Response(content, status=status.HTTP_200_OK)
