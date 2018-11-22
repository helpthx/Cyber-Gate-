# Faz o cadastrado de novos usarios no banco de dados SQLite 
# helpthx

''''
Capture infos about users. There r five filds, ID, nome, matricula, ru and acessos.
	==> Each user will have a unique numeric integer ID linked with a SQLite3 database call Banco_de_dados.db
    ==> Each ID has a name, matricula, amount of credit in RU and acessos.

Developed by João Vitor Rodrigues Baptista. 
'''

import sqlite3
import sys

def cadastrar_usuario(): 
	conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
	print ('Banco aberto com sucesso...');

	print('\n-----------------------------')
	nome = input('Digite o nome do aluno: ')
	matricula = input('Digite a matricula: ')
	print('-----------------------------\n')
	ru = 00.00
	acessos = 0

	conn.execute("INSERT INTO CADASTROS (NOME,MATRICULA,RU,ACESSOS) \
    	  VALUES (?, ?, ?, ?)", (nome,matricula,ru,acessos));

	conn.commit()
	print('Cadastro salvo com sucesso...');
	print('\n')
	conn.close()
	sys.exit(1)

cadastrar_usuario()