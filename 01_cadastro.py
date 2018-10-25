# Faz o cadastrado de novos usarios no banco de dados SQLite 
# helpthx

import sqlite3
import sys

def cadastrar_usuario(): 
	conn = sqlite3.connect('Banco_de_dados.db')
	print ('Banco aberto com sucesso...');

	#id_1 = input('Digite o ID: ')
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