from django.urls import path, include

from Apps.personas.views import *

urlpatterns = [
    path('', personas_listar.as_view(), name='personas_listar'),
    path('crear/', personas_crear.as_view(), name='personas_crear'),
    path('editar/<int:pk>/', personas_editar.as_view(), name='personas_editar'),
    path('eliminar/<int:pk>/', personas_eliminar.as_view(), name='personas_eliminar'),
]
