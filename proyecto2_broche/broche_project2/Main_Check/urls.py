#Creamos URLS para poder realizar la URLconfig y empezar a mostrar las vistas que aplicamos dentro de Main_Check

from django.urls import include, path
from Main_Check import views
from rest_framework import routers
from Main_Check.viewsets import recetaViewSet
from Main_Check.viewsets import clienteViewSet


router = routers.DefaultRouter()
router.register(r'receta', recetaViewSet.RecetaViewSet)
router.register(r'cliente', clienteViewSet.ClienteViewSet) 

urlpatterns = [
    path('parametros', views.index, name='parametros'),
    path('intento', views.funcion, name='esto-prueba'), #tratar de respetar minusculas para urls
    # Urls API
    path('api-recetas/', include(router.urls)),
    path('api-clientes/', include(router.urls)), #si dejo include(router.urls), me llama todas las urls del router?
]

#crear path de ahsfkasñdjgklñsadjgklñ paso final