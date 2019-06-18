from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from Apps.libros.models import Reserva, Persona, LibroModelo

def index(request):
    
    return render(request, 'index.html')

def libros(request):
    datos = LibroModelo.objects.all() # modelo
    response_json = serializers.serialize('json', datos)
    return HttpResponse(response_json, content_type='application/json')

def personas(request):
    datos = Persona.objects.all() # modelo
    response_json = serializers.serialize('json', datos)
    return HttpResponse(response_json, content_type='application/json')

def reservas(request):
    datos = Reserva.objects.all() # modelo
    response_json = serializers.serialize('json', datos)
    return HttpResponse(response_json, content_type='application/json')

def reservas_add(request):
    if request.method=='POST':
        libro =request.POST[libro]
        persona =request.POST[persona]
        if libro !="0" and persona !="0":
            reserva=Reserva(libro_id=libro, persona_id=persona)
            reserva.save()
        redirect('index')
    return render(request,'index.html')

