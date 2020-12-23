from django import forms
from .models import *

class Login(forms.ModelForm):
    class Meta:
        model = Administrador
        fields =("nombre","contra")
