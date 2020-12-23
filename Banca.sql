create database Banca;
use Banca;

create table ADMINISTRADOR(
Nombre varchar(15) not null,
contra varchar(20) not null,
primary key(Nombre)
);
insert into ADMINISTRADOR(Nombre,contra) values('admin','admin');
select * from clienteindividual;
create table clienteIndividual(
usuarioI varchar(20) primary key,
pass varchar(20),
cui bigint(20),
nit int(11),
nombre varchar(20),
apellido varchar(20),
fehcanac date,
telefono int(9)
);
create table USUARIOINDIVIDUAL(
CUI bigint(20) primary key,
NIT int(11),
nombres varchar(30),
apellidos varchar(30),
fechaNacimiento date
);

create table USUARIOEMPRESARIAL(
idUsuarioemp int auto_increment primary key,
tipoEmpresa enum('sociedad anonima','compañia limitada','empresa individual'),
nombre varchar(40),
nombreComercial varchar(40),
nombresRepresentante varchar(35),
apellidosRepresentante varchar(35)
);
create table USUARIO(
idUsuario int auto_increment primary key,
contra varchar(20),
CUI bigint(20),
idUsuarioemp int,
foreign key (CUI) references USUARIOINDIVIDUAL(CUI),
foreign key (idUsuarioemp) references USUARIOEMPRESARIAL(idUsuarioemp)
);

/*CAMPO DE PRUEBAS*/
insert into usuarioindividual values(12345,124,'loca ersr','erdsr fer','1985-08-12');
select * from usuarioindividual;
delete from usuarioindividual where cui=12345;
insert into usuario(contra,cui) values('123',123);
select * from usuario;
select * from usuarioindividual;
drop table usuarioempresarial;
drop table usuarioindividual;

