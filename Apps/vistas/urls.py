from django.urls import path

from Apps.vistas.views import *

urlpatterns = [
    path('', index, name='index'),
    path('libros/', libros, name='libros'),
    path('personas/', personas, name='personas'),
    path('reservas/', reservas, name='reservas'),
    path('reservas_add/', reservas_add, name='reservas_add'),

]