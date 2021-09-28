from django import forms
from .models import Administradores, Estudiante 

class EstudianteForms(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AdministradorForms(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = '__all__'

