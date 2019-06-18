from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Apps.libros.models import LibroModelo
from Apps.libros.forms import LibroForm

class listar(ListView):
	model = LibroModelo
	template_name = 'listar.html'

class crear(CreateView):
	model = LibroModelo
	form_class = LibroForm
	template_name = 'crear.html'
	success_url = reverse_lazy('listar')

class editar(UpdateView):
	model = LibroModelo
	form_class = LibroForm
	template_name = 'editar.html'
	success_url = reverse_lazy('listar')

class eliminar(DeleteView):
	model = LibroModelo
	template_name = 'eliminar.html'
	success_url = reverse_lazy('listar')
