''' Funções para editar as colunas do banco de dados  Créditos no RU/ Acessos
	helpthx
'''

import sqlite3
import sys
import sys, traceback
import os



def criar_tabela():
	conn = sqlite3.connect('Banco_de_dados.db')
	print('\nBanco aberto com sucesso...');

	conn.execute('''CREATE TABLE CADASTROS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NOME           TEXT    NOT NULL,
         MATRICULA            INT     NOT NULL,
         RU        	REAL NOT NULL,
         ACESSOS         INT NOT NULL);''')
	conn.execute('INSERT INTO CADASTROS VALUES (0, "USUARIO 0", 00000000 , 00.00, 0)')
	conn.commit()
	print('Tabela criada com sucesso...');
	print('\n')
	conn.close()
	sys.exit(1)

def recarregar_ru():
	conn = sqlite3.connect('Banco_de_dados.db')
	print('\nBanco aberto com sucesso...');
	
	matricula = input('Qual a matricula ?:  ')
	dinheiro = input('Quanto de dinheiro colocar ?:')
	float(dinheiro)
	conn.execute("UPDATE CADASTROS set RU = RU +" +dinheiro+ " WHERE  MATRICULA = "+ matricula);
	conn.commit()
	print('\nNumero total de colunas atualizadas: ', conn.total_changes)
	if conn.total_changes > 0:
		print('Alterado com sucesso...')
	else:
		print('Alguma operação deu errado...')

	print('\n')
	os.system('clear')
	conn.close()
	sys.exit(1)

def contador_acessos():
	conn = sqlite3.connect('Banco_de_dados.db')
	print('\nBanco aberto com sucesso...');
	print('---------------------------')
	MATRICULA1 = input('Digite a matricula: ')
	
	conn.execute('UPDATE CADASTROS set ACESSOS = ACESSOS+1 WHERE  MATRICULA='+MATRICULA1);
	conn.commit()
	print('Numero total de colunas atualizadas: ', conn.total_changes)
	if conn.total_changes > 0:
		print('Alterado com sucesso...')
	else:
		print('Alguma operação deu errado...')

	print('\n')
	os.system('clear')
	conn.close()
	sys.exit(1)

def loop_principal():
	print('------------------------------------------------------------------------------------------------------------------')
	print('1 -> Cria Tabela; 2 -> Adiona creditos no RU; 3 -> Contador de pessoas; 5 -> Sair: ')
	print('------------------------------------------------------------------------------------------------------------------')
	a = input()
	x = 1

	while(x):
		if int(a) == 1:
			criar_tabela()
			print('\nTabela Criada com sucesso...\n\n')
			a = 0;

		elif int(a) == 2:
			recarregar_ru()
			print('\nCredito adicionado com sucesso...\n\n')
			a = 0;
			
		elif int(a) == 90:
			#recarregar_ru()
			print('\nVc digitou 90, parabens vc é retardado\n\n')
			a = 0;

		elif int(a) == 3:
			contador_acessos()
			print('\nPessoa passou pela catraca...\n\n')
			a = 0;

		elif int(a) == 5:
			print('\nSaindo...\n\n')
			sys.exit(0)
			
		else:
			print('\nVoltando para o começo\n\n')
			loop_principal()


loop_principal()
