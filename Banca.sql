create database Banca;
use Banca;

create table ADMINISTRADOR(
Nombre varchar(15) not null,
contra varchar(20) not null,
primary key(Nombre)
);
insert into ADMINISTRADOR(Nombre,contra) values('administrador','admin');

create table USUARIOINDIVIDUAL(
CUI int(13) unsigned zerofill primary key,
NIT int(7) unsigned zerofill default null,
nombres varchar(35) not null,
apellidos varchar(35) not null,
fechaNacimiento date not null
);

create table USUARIOEMPRESARIAL(
idUsuarioemp int auto_increment primary key,
tipoEmpresa enum('sociedad anonima','compañia limitada','empresa individual'),
nombre varchar(40) not null,
nombreComercial varchar(40) not null,
nombresRepresentante varchar(35) not null,
apellidosRepresentante varchar(35) not null
);
create table USUARIO(
idUsuario int auto_increment primary key,
idTipoUsuario int not null,
CUI int(13) unsigned zerofill,
idUsuarioemp int,
foreign key (CUI) references USUARIOINDIVIDUAL(CUI),
foreign key (idUsuarioemp) references USUARIOEMPRESARIAL(idUsuarioemp)
);

