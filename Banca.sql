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
alter table USUARIO add deuda decimal(65,3);
DESC USUARIO;

create table CUENTA(
numerocuenta int auto_increment primary key,
idUsuario int,
tipomoneda enum('Q','$'),
estaActiva enum('si','no'),
foreign key(idUsuario)references USUARIO(idUsuario)
);

create table CUENTAMONETARIA(
numerocuenta int primary key,
preautoriza enum('si','no'),
nocheques int(2),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

create table CUENTAAHORRO(
numerocuenta int primary key,
interes int,
saldo decimal(35,3),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

create table CUENTAPF(
numerocuenta int primary key,
interes int,
saldo decimal(35,3),
tiempo enum('3','6','12','24'),
foreign key(numerocuenta) references CUENTA(numerocuenta)
);

/*CAMPO DE PRUEBAS*/
insert into usuarioindividual values(12345,124,'loca ersr','erdsr fer','1985-08-12');
select * from usuarioindividual;
delete from usuarioindividual where cui=12345;
insert into usuario(contra,cui) values('123',123);
select * from usuario;
select * from usuarioindividual;
select * from usuarioempresarial;

