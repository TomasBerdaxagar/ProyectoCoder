from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    esNoche = models.BooleanField(null=True)
    
    def __str__(self) :
        
        return f"CURSO {self.nombre} --- CAMADA {self.camada} --- ESNOCHE {self.esNoche}"
class Jugador(models.Model):
    
    apellido= models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
    
    def __str__(self) :
        
        return f"APELLIDO {self.apellido} --- NUMERO {self.numero} --- ESBUENO {self.esBueno}"
class Equipo(models.Model):
    
    nombre=models.CharField(max_length=40)
    ciudad=models.CharField(max_length=40)
    nombreHinchada=models.CharField(max_length=40)
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- CIUDAD {self.ciudad} --- NOMBREHINCHADA {self.nombreHinchada}"
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


class Arbitro(models.Model):

    nombre=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)
    edad=models.IntegerField()
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- NACIONALIDAD {self.nacionalidad} --- EDAD {self.edad} --- DIRIGEBIEN {self.dirigeBien}" 

class Seleccion(models.Model):
    
    nombre=models.CharField(max_length=40)
    continente=models.CharField(max_length=40)
    tecnico=models.CharField(max_length=40)
    
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- CONTINENTE {self.continente} --- TECNICO {self.tecnico}" 
    
 
class Arbitro(models.Model):

    nombre=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)
    edad=models.IntegerField()
    dirigeBien= models.BooleanField()
    def __str__(self) :
        
        return f"NOMBRE {self.nombre} --- NACIONALIDAD {self.nacionalidad} --- EDAD {self.edad} --- DIRIGEBIEN {self.dirigeBien}" 