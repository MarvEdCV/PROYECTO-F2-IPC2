# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    nombre = models.CharField(db_column='Nombre', primary_key=True, max_length=15)  # Field name made lowercase.
    contra = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'administrador'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    idtipousuario = models.IntegerField(db_column='idTipoUsuario')  # Field name made lowercase.
    cui = models.ForeignKey('Usuarioindividual', models.DO_NOTHING, db_column='CUI', blank=True, null=True)  # Field name made lowercase.
    idusuarioemp = models.ForeignKey('Usuarioempresarial', models.DO_NOTHING, db_column='idUsuarioemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarioempresarial(models.Model):
    idusuarioemp = models.AutoField(db_column='idUsuarioemp', primary_key=True)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='tipoEmpresa', max_length=18, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=40)
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=40)  # Field name made lowercase.
    nombresrepresentante = models.CharField(db_column='nombresRepresentante', max_length=35)  # Field name made lowercase.
    apellidosrepresentante = models.CharField(db_column='apellidosRepresentante', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarioempresarial'


class Usuarioindividual(models.Model):
    cui = models.IntegerField(db_column='CUI', primary_key=True)  # Field name made lowercase.
    nit = models.IntegerField(db_column='NIT', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarioindividual'
