from django.http import HttpResponse
import datetime
from django.template import Template,Context

class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido = apellido



def saludo(request): # primera vista

    p1= Persona("El Ángel","Salar")

    #nombre = "Ángel"
    #apellido = "Salar"

    temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ahora=datetime.datetime.now()

    doc_externo = open("C:/Users/UTSRADMIN01/Dropbox/Programación/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plantilla=Template(doc_externo.read())

    doc_externo.close()

    contexto=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temas_del_curso})

    documento=plantilla.render(contexto)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")

def dame_fecha(request):

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,agno):

    periodo=agno-2020
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendrás %s años" %(agno,edadFutura)

    return HttpResponse(documento)
