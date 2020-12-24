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

class CrearClienteEmpresarial(forms.ModelForm):
    class Meta:
        model = Usuarioempresarial
        fields = ("tipoempresa","nombre","nombrecomercial","nombresrepresentante","apellidosrepresentante")

class Intermedia(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ("idusuario","tipomoneda","estaactiva")

class Intermedia1(forms.Form):
    idusuario = forms.IntegerField(required=True)
    tipomoneda = models.CharField(max_length=1, blank=True, null=True)
    estaactiva = models.CharField(db_column='estaActiva', max_length=2, blank=True,
                                  null=True)  # Field name made lowercase.
    class Meta:
        fields = ("idusuario","tipomoneda","estaactiva")