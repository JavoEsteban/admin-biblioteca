from django import forms
from Apps.libros.models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = ['rut', 'nombres', 'apellidos', 'fono', 'email']

        labels = {
            'rut':'Rut',
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'fono':'Fono',
            'email':'E-Mail'
        }

        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'fono':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
    