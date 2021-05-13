from django.shortcuts import render

# Creando primera Vista Principal/Main

from django.http import HttpResponse

def index(request): #Recibo
    print("request --> ",request) #Proceso 
    return HttpResponse("Main Check: Primera vista") #retorno/resultado

def funcion(request):
    operando=2+3
    return HttpResponse(operando)

    
