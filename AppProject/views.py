from django.shortcuts import render
from django.http import HttpResponse
from AppProject.models import *
from AppProject.forms import *


def vista_inicio(request):
    return render(request, "AppProject/index.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["contrasenia"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "AppProject/registro.html", {"formulario": formulario})

def vista_pelicula(request):
    if request.method == "POST":
        formulario = PelisForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            peli = Pelicula(nombre_pelicula = data["nombre_pelicula"], director = data["director"], fecha_estreno = data["fecha_estreno"], sinopsis = data["sinopsis"])
            peli.save()
    formulario = PelisForm()
    return render(request, "AppProject/pelicula.html", {"formulario": formulario})

def vista_estrenos(request):
    if request.method == "POST":
        formulario = EstrenosForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            estreno = Estreno(nombre_estreno = data["nombre_estreno"], fecha_estreno = data["fecha_estreno"])
            estreno.save()
    formulario = EstrenosForm()
    return render(request, "AppProject/estrenos.html", {"formulario": formulario})

def vista_inicio_sesion(request):
    return render(request, "AppProject/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "AppProject/busqueda.html")

def vista_resultado(request):
    nombre_pelicula = request.GET["nombre_pelicula"]
    pelicula = Pelicula.objects.filter(nombre_pelicula__icontains=nombre_pelicula)
    return render(request, "AppProject/resultados_busqueda.html", {"pelicula":pelicula})
    