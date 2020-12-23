from django import forms
from adminapp.models import *

class Login(forms.ModelForm):
    class Meta:
        model = Administrador
        fields =("nombre","contra")

class CrearClienteIndividual(forms.ModelForm):
    class Meta:
        model = Usuarioindividual
        fields = ("cui","nit","nombres","apellidos","fechanacimiento")
