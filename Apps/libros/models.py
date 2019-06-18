from django.db import models

class LibroModelo(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    edicion = models.IntegerField()
    copias = models.IntegerField()

    def __str__(self):
        return self.titulo+' '+self.autor

class Persona(models.Model):
    rut = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fono = models.IntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombres+' '+self.apellidos
		
class Reserva(models.Model):
    libro = models.ForeignKey(LibroModelo, null=False, blank=False, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libro.titulo+ ' '+self.persona.nombres 