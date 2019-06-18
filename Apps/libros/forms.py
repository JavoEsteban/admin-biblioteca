from django import forms

from Apps.libros.models import LibroModelo

class LibroForm(forms.ModelForm):
    class Meta:
        model = LibroModelo

        fields = [
            'titulo',
            'materia',
            'autor',
            'edicion',
            'copias'
        ]

        labels = {
            'titulo':'Título',
            'materia':'Materia',
            'autor':'Autor',
            'edicion':'Edición',
            'copias':'Num. Copias'
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'materia':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control'}),
            'edicion':forms.NumberInput(attrs={'class':'form-control'}),
            'copias':forms.NumberInput(attrs={'class':'form-control'})
        }