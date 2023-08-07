# importamos render para mostrar una pagina web, redirect para redireccionar y get_object_or_4040 para mostrar página 404
from django.shortcuts import render, redirect, get_object_or_404
# Permite guardar usuarios en la DB
from django.contrib.auth.models import User
# Utilizar clase para crear formularios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Utilizar login (cookie)
from django.contrib.auth import login, logout, authenticate
# importar formularios
from .forms import MilitarForm, PermisoForm, LicenciasForm
# importar modelos 
from .models import Militar, Permiso, Licencias
# proteger las urls de accesos no autorizados
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        
        if user is None:
            return render(request, 'index.html', {
            'form' : AuthenticationForm,
            'error' : 'Usuario o Contraseña inválidos'
        })
        
        else:
            login(request, user)
            return redirect('home')

@login_required(login_url='index')
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def home(request):
    militares = Militar.objects.all()
    return render(request,  'home.html',{
        'militares' : militares
    })

@login_required(login_url='index')
def agregar_militar(request):
    if request.method == 'GET':
        return render(request, 'agregar_militar.html', {
            'form' : MilitarForm
        })
    else:
        try:
            form = MilitarForm(request.POST)
            nuevo_militar = form.save(commit = False)
            nuevo_militar.save()
            return redirect('agregar_militar')
        except ValueError:
            return render(request,'agregar_militar.html', {
                'form' : MilitarForm,
                'error' : 'Proporciona los datos'
            })

@login_required(login_url='index')       
def agregar_permiso(request):
    if request.method == 'GET':
        return render(request, 'agregar_permiso.html', {
            'form' : PermisoForm
        })
    else:
        try:
            form = PermisoForm(request.POST)
            nuevo_permiso = form.save(commit = False)
            nuevo_permiso.save()
            return redirect('agregar_permiso')
        except ValueError:
            return render(request, 'agregar_permiso.html', {
                'form' : PermisoForm,
                'error' : 'Datos erroneos'
            })

@login_required(login_url='index')
def agregar_licencia(request)      :
    if request.method == 'GET':
        return render(request, 'agregar_licencia.html', {
            'form' : LicenciasForm
        })
    else:
        try:
            form = LicenciasForm(request.POST)
            new_licencia = form.save(commit = False)
            new_licencia.save()
            return redirect('agregar_licencia')
        except ValueError:
            return render(request, 'agregar_licencia.html', {
                'form' : LicenciasForm,
                'error' : 'Datos erroneos'
            })