from django.db import models

# Create your models here.
class Militar(models.Model):
    grado = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    matricula = models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre
    
class Permiso(models.Model):
    fecha = models.DateField()
    motivo = models.TextField()
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()
    militar = models.ForeignKey(Militar, on_delete = models.CASCADE)
    def __str__(self):
        return self.militar.nombre
    
class Licencias(models.Model):
    fecha = models.DateField()
    inicio = models.DateField(auto_now=False, auto_now_add=False)
    termino = models.DateField(auto_now=False, auto_now_add=False)
    militar = models.ForeignKey(Militar, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.militar.nombre