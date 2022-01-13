from django.urls import path #Importamos el path
from AppCoder import views # Importamos las vistas
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),

    path('jugadores/', views.jugadores, name="Jugadores"),
    path('jugadorFormulario', views.jugadorFormulario, name="JugadorFormulario"),
    path('leerJugadores', views.leerJugadores, name="LeerJugadores"),
    path('eliminarJugador/<numero_para_borrar>/', views.eliminarJugador, name="EliminarJugador"),
    path('editarJugador/<numero_para_editar>/', views.editarJugador, name="EditarJugador"),

    path('estadios/', views.estadios, name="Estadios"),
    path('estadioFormulario/', views.estadioFormulario, name="EstadioFormulario"),

    path('ligas/', views.ligas, name="Ligas"),
    path('ligaFormulario/', views.ligaFormulario, name="LigaFormulario"),

    path('quienesSomos/', views.quienesSomos, name="QuienesSomos"),

    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
    


]
