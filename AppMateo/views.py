from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

# Create your views here.


def familiar(request):
    integrante1= Familiar(nombre="Silvia", edad=58)
    integrante1.save()
    integrante2= Familiar(nombre="Marcelo", edad=58)
    integrante2.save()
    integrante3=Familiar(nombre="Mariano", edad=21)
    integrante3.save()
    integrante4= Familiar(nombre="Mateo", edad=22)
    integrante4.save()
    lista_familiares=[integrante1, integrante2, integrante3, integrante4]
    cadena= "El integrante: " + integrante1.nombre + "edad" + str(integrante1.edad)
    return render (request, "AppMateo/index.html", {"familiares": lista_familiares })
    return HttpResponse(cadena)