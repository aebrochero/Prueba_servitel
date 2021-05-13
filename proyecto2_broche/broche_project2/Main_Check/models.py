from django.db import models

class Receta(models.Model): #recibe un modelo
    nombre = models.CharField(max_length=200) #models. obtener las funcionalidades de los modelos
    ingredientes = models.CharField(max_length=100) #Crear migracion cada vez que se crea/borra/actualiza cualquier cosa de un modelo
    autor = models.CharField(max_length=50, blank=True, null=True) 
    # autor = models.CharField(max_length=50, blank=True, null=True, default="hola") se puede hacer con blank+null o default
    rating = models.IntegerField(default=0)
    valor = models.IntegerField(blank=True, null=True)
    origen = models.CharField(blank=True, null=True, max_length=90)
    calorias = models.IntegerField(blank=True, null=True)
    correo = models.EmailField(blank=True, null=True, max_length=254)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField('Fecha de publicacion')
    fecha_modificacion = models.DateTimeField(auto_now=True)

    #definiendo un self: funcion que llama una variable/objeto/cosa que ya hemos utilizado
    #en este caso retorna el nombre usado en Class Receta
    #Si se define nombre dentro de la función y se usa return nombre, retornara el valor almacenado en "nombre" de solo la funcion
    def __str__(self):     
        return self.nombre

class Cliente(models.Model): #recibe un modelo en este caso clientes
    
    nombre_cliente = models.CharField(max_length=50, blank=False)
    apellido_cliente = models.CharField(max_length=50, blank=False) #como hacer campo obligatorio : blank:False
    segundo_apellido_cliente= models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=999) 
    telefono = models.IntegerField(blank=True, null=True)
    correo_cliente = models.EmailField(blank=True, null=True, max_length=254) 
    contraseña_cliente = models.CharField(blank=False, max_length=20)
    fecha_creacion_cliente = models.DateTimeField(auto_now_add=True) 
    foto = models.ImageField(blank=True, null=True, upload_to=None, height_field=None, width_field=None, max_length=100) #foto subir

    def __str__(self):     
        return self.nombre_cliente

