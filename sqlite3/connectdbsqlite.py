
import sqlite3


conn = sqlite3.connect('clientes.db')
curr = conn.cursor()


def create_table():
    
    curr.execute('CREATE TABLE registro ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
    'nome VARCHAR(20),'
    'status VARCHAR(10))')

def data_insert(dados):
    
    curr.execute('INSERT INTO registro (nome, status) VALUES (?,?)', dados)
    conn.commit()

def data_read_all():
    curr.execute('SELECT * FROM registro')
    dados = curr.fetchall()
    
    for linha in dados:
        print(linha)

def data_read_nome():
    curr.execute('SELECT nome FROM registro')
    dados = curr.fetchall()
    
    for linha in dados:
        print(linha)

        