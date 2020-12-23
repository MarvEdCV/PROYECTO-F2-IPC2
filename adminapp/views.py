from django.shortcuts import render
from .forms import *
import MySQLdb
from django.db.models import Q
# Create your views here.

host = 'localhost'
db_name = 'Banca'
user = 'root'
contra = 'Marvinkata'
puerto = 3306


def login(request):
    consulta = Administrador.objects.filter(nombre="admin").values_list()
    form = Login()
    variables = {
        "form": form,
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

def adminCrearCliente(request):
    form = CrearClienteIndividual()
    mensaje = ''
    variable={
        "form": form,
        "mensaje": mensaje
    }
    if request.method == "POST":
        form = CrearClienteIndividual(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cui = datos.get("cui")
            nit = datos.get("nit")
            nombres = datos.get("nombres")
            apellidos = datos.get("apellidos")
            fechanacimiento = datos.get("fechanacimiento")
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO USUARIOINDIVIDUAL(cui,nit,nombres,apellidos,fechanacimiento) VALUES(" + str(cui) +","+str(nit)+",'" +nombres+"','"+apellidos+"','"+str(fechanacimiento)+ "')"
            consulta1 = "INSERT INTO USUARIO(contra,cui) VALUES("+str(cui)+","+str(cui)+")"
            c.execute(consulta)
            c.execute(consulta1)
            db.commit()
            c.close()
            form = CrearClienteIndividual()
            z = Usuario.objects.filter(cui=str(cui)).values_list()
            print(z)
            mensaje = "SU USUARIO ES:----> "+str(z[0][0])+"  Y SU CONTRASEÑA ES-----> "+str(cui)
            variable = {
                "form": form,
                "mensaje": mensaje
            }

        else:
            form = CrearClienteIndividual()
            mensaje = "Ingrese datos"
            variable = {
                "form": form,
                "mensaje": mensaje
            }
    return render(request,'adminCrearCliente.html',variable)
