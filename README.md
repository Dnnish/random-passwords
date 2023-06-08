# random-passwords
Este es un mini proyecto para practicar python, lo que hace es generar contraseñas aleatorias y tiene para elegir 
la cantidad de contraseñas al crear y la longitud de las contraseñas que se vayan a generar. 
Al darle al botón de "Generar" creara las contraseñas y tambien hara el insert a la base de datos.

## DML mysql
create database pythonPrueba;
use pythonPrueba;

create table passwords (
id int auto_increment,
con_contraseña varchar(10) not null,
primary key CON_PK(id)
);
