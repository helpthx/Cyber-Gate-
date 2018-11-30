import sqlite3
import sys
import sys, traceback
import os


def zerar_acessos():
	conn = sqlite3.connect('Banco_de_dados.db')
	print('\nBanco aberto com sucesso...');
	print('---------------------------')
		
	conn.execute('UPDATE CADASTROS set ACESSOS = 0');
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

zerar_acessos();