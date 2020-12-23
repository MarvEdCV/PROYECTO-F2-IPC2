from django.shortcuts import render
from .forms import *
import MySQLdb
from django.db.models import Q
# Create your views here.


def login(request):
    consulta = Administrador.objects.filter(nombre="admin").values_list()
    form = Login()
    mensaje = ''
    variables = {
        "form": form,
        "mensaje": mensaje
    }
    if request.method == 'POST':
        form = Login(data=request.POST)
        datos = form.data
        name = datos.get("nombre")
        passw = datos.get("contra")
        if name == str(consulta[0][0]) and passw == str(consulta[0][1]):
            return render(request,'adminoperaciones.html')
    return render(request, 'adminlogin.html', variables)

def adminoperaciones(request):
    return render(request,'adminoperaciones.html')