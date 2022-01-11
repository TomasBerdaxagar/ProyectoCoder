from django.urls import path #Importamos el path
from AppCoder import views # Importamos las vistas

urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('jugadores/', views.jugadores, name="Jugadores"),
    path('equipos/', views.equipos, name="Equipos"),
    path('estadios/', views.estadios, name="Estadios"),
    path('estadioFormulario/', views.estadioFormulario, name="EstadioFormulario"),
    path('ligas/', views.ligas, name="Ligas"),
    path('ligaFormulario/', views.ligaFormulario, name="LigaFormulario"),
    path('arbitros/', views.arbitros, name="Arbitros"),
    path('arbitroFormulario/', views.arbitroFormulario, name="ArbitroFormulario"),
    path('selecciones/', views.selecciones, name="Selecciones"),
    path('seleccionFormulario/', views.seleccionFormulario, name="SeleccionFormulario"),



]