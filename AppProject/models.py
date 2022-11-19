from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

class Pelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    fecha_estreno = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length = 500)

class Estreno(models.Model):
    nombre_estreno = models.CharField(max_length = 500)
    fecha_estreno = models.CharField(max_length=50)

