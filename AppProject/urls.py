from django.urls import path
from AppProject.views import *

urlpatterns = [
    path("", vista_inicio, name = "des-inicio"),
    path("registro/", vista_registro, name = "des-registro"),
    path("pelicula/", vista_pelicula, name = "des-pelicula"),
    path("estreno/", vista_estrenos, name="des-estrenos"),
    path("iniciar_sesion/", vista_inicio_sesion, name="des-iniciar-sesion"),
    path("busqueda/", vista_busqueda, name="des-busqueda"),
    path("resultado_busqueda/", vista_resultado, name="des-busqueda-resultado")
]