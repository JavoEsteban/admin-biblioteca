from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('Apps.libros.urls')),
    path('personas/', include('Apps.personas.urls')),
    path('reservas/', include('Apps.reservas.urls')),
    path('vistas/', include('Apps.vistas.urls')),
]
