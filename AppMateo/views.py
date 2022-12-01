from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

# Create your views here.


def familiares(request):
    integrante1= Familiar(nombre="Mateo", edad=22)
    integrante1.save()
    return render (request, "AppMateo/index.html", {"familiar1": f"Ha creado {integrante1} a este integrante"})