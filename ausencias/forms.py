from django import forms
from .models import Militar, Permiso

class MilitarForm(forms.ModelForm):
    class Meta:
        model = Militar
        fields = [
            'grado',
            'nombre',
            'matricula',
        ]

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = [
            'fecha'
        ]