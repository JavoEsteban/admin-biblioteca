from django.urls import path, include

from Apps.libros.views import *

urlpatterns = [
    path('', listar.as_view(), name='listar'),
    path('crear/', crear.as_view(), name='crear'),
    path('editar/<int:pk>/', editar.as_view(), name='editar'),
    path('eliminar/<int:pk>/', eliminar.as_view(), name='eliminar'),
]
