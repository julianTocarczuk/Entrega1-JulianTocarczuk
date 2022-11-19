from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nombre_usuario = forms.CharField()
    contrasenia = forms.CharField()

class PelisForm(forms.Form):
    nombre_pelicula = forms.CharField()
    director = forms.CharField()
    fecha_estreno = forms.CharField()
    sinopsis = forms.CharField()

class EstrenosForm(forms.Form):
     nombre_estreno = forms.CharField()
     fecha_estreno = forms.CharField()
