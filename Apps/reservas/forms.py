from django import forms
from Apps.libros.models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva

        fields = ['libro', 'persona']

        labels = {
            'libro':'Libro',
            'persona':'Persona'
        }

        widgets = {
            'libro':forms.Select(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'})
        }
    