from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

class Jugador(models.Model):
    
    apellido= models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
    
    def __str__(self) :
        
        return f"APELLIDO {self.apellido} --- NUMERO {self.numero} --- ESBUENO {self.esBueno}"

class Estadio(models.Model):
    
    nombre=models.CharField(max_length=40)
    capacidad=models.IntegerField()
    direccion=models.CharField(max_length=40)
    anioFundacion=models.IntegerField()
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- CAPACIDAD {self.capacidad} --- DIRECCION {self.direccion} --- ANIOFUNDACION {self.anioFundacion}"

class Liga(models.Model):
    
    nombre=models.CharField(max_length=40)
    cantidadDeEquipos=models.IntegerField()
    pais=models.CharField(max_length=40)
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- CANTIDAD DE EQUIPOS {self.cantidadDeEquipos} --- PAIS {self.pais}" 


class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)


class QuienesSomos(models.Model):
    
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    
    
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- APELLIDO {self.apellido}"
