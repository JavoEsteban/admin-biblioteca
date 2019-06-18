from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from Apps.libros.models import Reserva, Persona, LibroModelo
from Apps.reservas.forms import ReservaForm

class reservas_listar(ListView):
    model = Reserva
    template_name = 'reservas_listar.html'

class reservas_crear(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas_crear.html'
    success_url = reverse_lazy('reservas_listar')

class reservas_editar(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas_editar.html'
    success_url = reverse_lazy('reservas_listar')

class reservas_eliminar(DeleteView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas_eliminar.html'
    success_url = reverse_lazy('reservas_listar')
