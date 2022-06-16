from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familia
from django.template import Template, Context, loader

# Create your views here.
def papa(self):

    datos= Familia(nombre="Pablito", edad="50", nacimiento="1970-12-30" )
    datos.save()

    documento=f"Nombre: {datos.nombre}, Edad: {datos.edad}, Nacimiento: {datos.nacimiento}"


    return HttpResponse(documento)

def mama(self):

    datos= Familia(nombre="Laura", edad="40", nacimiento="1969-10-07" )
    datos.save()

    documento=f"Nombre: {datos.nombre}, Edad: {datos.edad}, Nacimiento: {datos.nacimiento}"

    return HttpResponse(documento)

def broda(self):

    datos= Familia(nombre="Karel", edad="15", nacimiento="2007-03-01" )
    datos.save()

    documento=f"Nombre: {datos.nombre}, Edad: {datos.edad}, Nacimiento: {datos.nacimiento}"

    return HttpResponse(documento)

def yo(self):

    datos= Familia(nombre="Jurgen", edad="23", nacimiento="1999-01-07" )
    datos.save()

    documento=f"Nombre: {datos.nombre}, Edad: {datos.edad}, Nacimiento: {datos.nacimiento}"

    return HttpResponse(documento)

def Ptemplate(self):

    nombre ="Jurgen"
    ap="Almiralla"

