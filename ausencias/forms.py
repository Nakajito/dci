from django.forms import ModelForm
from django import forms
from .models import Militar, Permiso, Licencias

class MilitarForm(ModelForm):
    class Meta:
        model = Militar
        fields = [
            'grado',
            'nombre',
            'matricula',
        ]
        
        widgets = {
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PermisoForm(ModelForm):
    class Meta:
        model = Permiso
        fields = [
            'fecha',
            'motivo',
            'hora_llegada',
            'hora_salida',
            'militar'
        ]
        
        widgets = {
            'fecha' : forms.DateInput(attrs = {'type' : 'date', 'class' : 'form-control'}),
            'motivo' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'hora_llegada' : forms.TextInput(attrs = {'type' : 'time', 'class' : 'form-control'}),
            'hora_salida' : forms.TextInput(attrs = {'type' : 'time', 'class' : 'form-control'}),
            'militar' : forms.Select(attrs = { 'class' : 'form-control'})
            
        }

class LicenciasForm(forms.ModelForm):
    class Meta:
        model = Licencias
        fields = [
            'fecha',
            'motivo',
            'inicio',
            'termino',
            'militar'
        ]
        
        widgets = {
            'fecha' : forms.DateInput(attrs = {'type' : 'date', 'class' : 'form-control'}),
            'motivo' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'inicio' : forms.TextInput(attrs = {'type' : 'date', 'class' : 'form-control'}),
            'termino' : forms.TextInput(attrs = {'type' : 'date', 'class' : 'form-control'}),
            'militar' : forms.Select(attrs = { 'class' : 'form-control'})
            
        }