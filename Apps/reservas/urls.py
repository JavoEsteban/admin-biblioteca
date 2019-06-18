from django.urls import path

from Apps.reservas.views import *

urlpatterns = [
    path('', reservas_listar.as_view(), name='reservas_listar'),
    path('crear/', reservas_crear.as_view(), name='reservas_crear'),
    path('editar/<int:pk>', reservas_editar.as_view(), name='reservas_editar'),
    path('eliminar/<int:pk>', reservas_eliminar.as_view(), name='reservas_eliminar'),
]

