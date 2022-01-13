from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Estadio, Liga, Jugador, Avatar, QuienesSomos

from AppCoder.forms import EstadioFormulario, JugadorFormulario, UserRegisterForm, UserEditForm, AvatarFormulario

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required




def editarJugador(request, numero_para_editar): 
    
   
    
    jugador = Jugador.objects.get(numero=numero_para_editar)
    #id, numero, nombre, esBueno
    
   
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
          
                
            #id
            jugador.apellido = informacion["apellido"]
            jugador.numero = informacion["numero"]
            jugador.esBueno = informacion["esBueno"]
              
            
            
            jugador.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = JugadorFormulario(initial={"apellido":jugador.apellido,"numero":jugador.numero,"esBueno":jugador.esBueno})
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/editarJugador.html',{"miFormulario":miFormulario,"numero_para_editar":numero_para_editar})


def eliminarJugador(request, numero_para_borrar):
    
    jugadorQueQuieroBorrar = Jugador.objects.get(numero=numero_para_borrar)
    jugadorQueQuieroBorrar.delete()
    
    
    jugadores = Jugador.objects.all()
    
    return render(request, "AppCoder/leerJugadores.html", {"jugadores":jugadores} )


@login_required
def leerJugadores(request):
    
    jugadores = Jugador.objects.all()
    
    dir = {"jugadores":jugadores} #contexto
    
    return render(request, "AppCoder/leerJugadores.html", dir)




# Create your views here.


#Formularios
@login_required
def estadioFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":

        miFormulario = EstadioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
        
            estadio = Estadio( nombre = informacion['nombre'], capacidad = informacion['capacidad'], direccion = informacion['direccion'], anioFundacion = informacion['anioFundacion'] )
        
            estadio.save()
        
            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario = EstadioFormulario()
        
    
    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})


def jugadorFormulario(request):
    
    #obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
            juga = Jugador(
                
                apellido = informacion["apellido"],
                numero = informacion["numero"],
                esBueno = informacion["esBueno"]
                  
            )
            
            juga.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = JugadorFormulario()
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/jugadorFormulario.html',{"miFormulario":miFormulario})



def ligaFormulario(request):
    
    #obtiene los valores
    if request.method == "POST":
        
        liga = Liga( nombre = request.POST['nombre'], cantidadDeEquipos = request.POST['cantidadDeEquipos'], pais = request.POST['pais'])
        
        liga.save()
        
        return render(request, 'AppCoder/inicio.html')
        
    
    return render(request, 'AppCoder/ligaFormulario.html')







#Primer vista
def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html', diccionario)

def jugadores(request):

    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/jugadores.html')

def estadios(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/estadios.html')

def ligas(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/ligas.html')


def quienesSomos(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/quienesSomos.html')






def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contraseña)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS INCORRECTOS"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )


def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Creado"})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})



@login_required
def editarPerfil(request):
    
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})
