
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
