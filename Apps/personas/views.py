from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from Apps.libros.models import Persona
from Apps.personas.forms import PersonaForm


class personas_listar(ListView):
    model = Persona
    template_name = 'personas_listar.html'

class personas_crear(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas_crear.html'
    success_url = reverse_lazy('personas_listar')

class personas_editar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas_crear.html'
    success_url = reverse_lazy('personas_listar')

class personas_eliminar(DeleteView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas_eliminar.html'
    success_url = reverse_lazy('personas_listar')





