/* Modelagem Basica */

CLIENTE

NOME - CARACTER (30)
CPF - NUMERICO (11)
EMAIL - CARACTER (30)
TELEFONE - CARACTER (30)
ENDERECO - CARACTER (100)
SEXO CARACTER (1)

/* Iniciando a modelagem fisica*/
/* CRIANDO O BANCO DE DADOS */

CREATE DATABASE PROJETO;

/* CONECTANDO-SE AO BANCO*/

USE PROJETO

/* CRIANDO TABELA CLIENTES*/
CREATE TABLE CLIENTE (
	NOME VARCHAR(30),
	CPF INT(11),
	EMAIL VARCHAR(30),
	TELEFONE VARCHAR(30),
	ENDERECO VARCHAR (100),
	SEXO CHAR(1)
);

/*VERIFICANDO TABELAS DO BANCO*/
SHOW TABLES;

/* DESCOBRINDO A ESTRUTURA DA TABELA*/
DESC CLIENTE;


/* OMITINDO COLUNA*/
/* SINTAXE BASICA DE INSERÇÃO - INSERT INTO TABELA*/

INSERT INTO CLIENTE VALUES('JOAO','M','JOAO@GMAIL.COM',988638273,'22923110','MAIA LACERDA - ESTACIO - RIO DE JANEIRO - RJ');

INSERT INTO CLIENTE VALUES('CELIA','F','CELIA@GMAIL.COM',541521456,'25078869','RIACHUELO - CENTRO - RIO DE JANEIRO - RJ');

INSERT INTO CLIENTE VALUES('JORGE','M',NULL,885755896,'58748895','OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG');

/* FORMA 02 - COLOCANDO AS COLUNAS */

INSERT INTO CLIENTE(NOME,SEXO,ENDERECO,TELEFONE,CPF) VALUES('LILIAN','F','SENADOR SOARES - TIJUCA - RIO DE JANEIRO - RJ','947785696',887774856);
INSERT INTO CLIENTE(NOME,SEXO,EMAIL,CPF,TELEFONE,ENDERECO) VALUES('JOAO','M','JOAO@GMAIL.COM',988638273,'22923110','MAIA LACERDA - ESTACIO - RIO DE JANEIRO - RJ');
INSERT INTO CLIENTE(NOME,SEXO,EMAIL,CPF,TELEFONE,ENDERECO) VALUES ('JORGE','M',NULL,885755896,'58748895','OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG');
INSERT INTO CLIENTE(NOME,SEXO,EMAIL,CPF,TELEFONE,ENDERECO) VALUES('CELIA','F','CELIA@GMAIL.COM',541521456,'25078869','RIACHUELO - CENTRO - RIO DE JANEIRO - RJ');


/* FORMA 03 - INSERT COMPACTO - SOMENTE MYSQL */

INSERT INTO CLIENTE VALUES('ANA','F','ANA@GLOBO.COM',85548962,'548556985','PRES ANTONIO CARLOS - CENTRO - SAO PAULO - SP'),
                          ('CARLA','F','CARLA@TERATI.COM.BR',7745828,'66587458','SAMUEL SILVA - CENTRO - BELO HORIZONTE - MG');
						  
INSERT INTO CLIENTE(NOME,SEXO,ENDERECO,TELEFONE,CPF) VALUES('CLARA','F','SENADOR SOARES - TIJUCA - RIO DE JANEIRO - RJ','883665843',99999999999);

INSERT INTO CLIENTE(NOME,SEXO,ENDERECO,TELEFONE,CPF) VALUES('CLARA','F','SENADOR SOARES - TIJUCA - RIO DE JANEIRO - RJ','883665843',22222222222);

